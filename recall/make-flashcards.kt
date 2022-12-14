//usr/bin/env [ $0 -nt $0.jar ] && kotlinc -d $0.jar $0; [ $0.jar -nt $0 ] && java -cp $CLASSPATH:$0.jar Make_flashcardsKt "$@"; exit 0

val usage = """
usage: make-flashcards.kt [ {name} | help | test ]

reads from stdin
writes to name.xxx.png, where xxx is the flashcard number
each line describes a flashcard with the question and answer separated by a colon
blank lines are ignored
lines starting with == start a new heading
"""

fun main(args: Array<String>) {
    if (args.isEmpty()) {
        processStdin()
    } else {
        when (args[0]) {
            "test" -> test()
            "help" -> print(usage)
            else -> print(usage)
        }
    }
}

data class Card(
    val question: String, 
    val answer: String,
    val category: String = ""
)

// simple test functions, since kotlin.test is not on the default classpath
fun test(klass: Class<*> = ::test.javaClass.enclosingClass, prefix: String = "def_") {
    klass.declaredMethods.filter { it.name.startsWith(prefix) }.forEach { it(null) }
}
infix fun Any?.returns(result: Any?) { 
    if (this != result) throw AssertionError("Expected: $result, got $this") 
}
infix fun (() -> Any).throws(ex: kotlin.reflect.KClass<out Throwable>) { 
    try { 
        invoke() 
        throw AssertionError("Exception expected: $ex")
    } catch (e: Throwable) { 
        if (!ex.java.isAssignableFrom(e.javaClass)) throw AssertionError("Expected: $ex, got $e")
    } 
}

fun def_parseLabelledCards() {
    "".parseLabelledCards() returns listOf<Card>()
    "foo: bar".parseLabelledCards() returns listOf(Card("foo", "bar"))
    "foo : bar".parseLabelledCards() returns listOf(Card("foo", "bar"))
    "foo :label bar".parseLabelledCards() returns listOf(Card("foo :label", "bar"))
    "foo:label bar".parseLabelledCards() returns listOf(Card("foo :label", "bar"))
    "foo : bar : baz".parseLabelledCards() returns 
            listOf(Card("foo :1", "bar"), Card("foo :2", "baz"))
    "foo: bar :label baz".parseLabelledCards() returns 
            listOf(Card("foo :1", "bar"), Card("foo :label", "baz"))
    "foo : bar :label baz".parseLabelledCards() returns 
            listOf(Card("foo :1", "bar"), Card("foo :label", "baz"))
    "foo :label bar : baz".parseLabelledCards() returns
            listOf(Card("foo :label", "bar"), Card("foo :2", "baz"))
}
fun String.parseLabelledCards(category: String = ""): List<Card> {
    val separators = separatorRegex.findAll(this).map { it.range }.toList()
    if (separators.isEmpty()) {
        return emptyList<Card>()
    } else {
        val baseQuestion = take(separators[0].first).trim() + " "
        return separators.mapIndexed { i, range ->
            val question = baseQuestion + if (range.count() > 1) {
                drop(range.first).take(range.count())
            } else if (separators.size > 1) {
                ":" + (i + 1)
            } else {
                ""
            }
            val answer = if (i == separators.lastIndex) {
                drop(range.last + 1)
            } else {
                drop(range.last + 1).take(separators[i + 1].first - range.last - 1)
            }
            Card(question.trim(), answer.trim(), category)
        }
    }
}
val separatorRegex = Regex(":[^ ]*")

fun def_parseUnlabelledCards() {
    "".parseUnlabelledCards() returns listOf<Card>()
    "foo: bar".parseUnlabelledCards() returns listOf(Card("foo", "bar"))
    "foo : bar".parseUnlabelledCards() returns listOf(Card("foo", "bar"))
    "foo : bar : baz".parseUnlabelledCards() returns
            listOf(Card("foo", "bar"), Card("foo : bar", "baz"))
    "foo : bar : baz : zap".parseUnlabelledCards() returns
            listOf(Card("foo", "bar"), Card("foo : bar", "baz"), Card("foo : bar : baz", "zap"))
}
fun String.parseUnlabelledCards(category: String = ""): List<Card> {
    val parts = split(":")
    if (parts.size < 2) {
        return emptyList<Card>()
    } else {
        var result = mutableListOf<Card>()
        var question = StringBuilder(parts[0].trim())
        parts.drop(1).forEach {
            val answer = it.trim()
            result.add(Card(question.toString(), answer, category))
            question.append(" : ").append(answer)
        }
        return result
    }
}

fun def_wrap() {
    "12345".wrap(1) returns "1\n2\n3\n4\n5"
    "12345".wrap(2) returns "12\n34\n5"
    "12345".wrap(5) returns "12345"
    "12345".wrap(6) returns "12345"
    "1\n2345".wrap(2) returns "1\n23\n45"
    "12\n345".wrap(2) returns "12\n34\n5"
    "12\n345".wrap(3) returns "12\n345"
}
fun String.wrap(width: Int): String {
    var i = 0
    return asSequence().fold(StringBuilder()) { acc, ch -> 
        if (i > 0 && i % width == 0 && ch != '\n') acc.append("\n")
        if (ch == '\n') i = 0 else i++
        acc.append(ch)
    }.toString()
}

fun makeFlashcard(card: Card, heading: String, filename: String) {
    val question = "$heading\n${card.category}\n${card.question.wrap(15)}"
    val answer = card.answer.wrap(15)
    Runtime.getRuntime().exec(arrayOf(
        "convert", "-size", "240x320", "xc:black",
        "-font", "FreeMono", "-weight", "bold", "-pointsize", "24",
        "-fill", "white", "-annotate", "+12+24", question,
        "-fill", "yellow", "-annotate", "+12+185", answer,
        "$filename"))
}

fun processStdin() {
    var song = ""
    var songs = 0
    var lines = 0
    var category = ""
    var categories = 0
    System.`in`.bufferedReader().lines().forEach { line ->
        if (line.matches(headerRegex)) {
            song = line.drop(17).takeWhile { it != '/' && it != '@' }.trim().replace(" ", "-")
            songs++
            categories = 0
        } else if (line.startsWith("==")) {
            category = line.drop(2).lowercase()
            categories++
            lines = 0
        } else if (line.isNotBlank()) {
            lines++
            line.parseUnlabelledCards(category).forEachIndexed { i, card ->
                if (card.answer.isNotBlank()) {
                    val dir = "00$song" // "00$categories$i.$category"
                    val seq = "%d%d%02d%02d".format(categories, i, songs, lines)
                    mkdir(dir)
                    makeFlashcard(card, song, "$dir/$seq.$song.png")
                }
            }
        }
    }
}
val headerRegex = Regex("^[0-9A-Z_]{13} \\|.*$")
fun mkdir(dir: String) = java.io.File(dir).mkdir()

