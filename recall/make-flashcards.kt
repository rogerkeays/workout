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
        print(usage)
    } else {
        when (args[0]) {
            "help" -> print(usage)
            "test" -> test()
            else -> processStdin(args[0])
        }
    }
}

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

fun makeFlashcard(name: String, heading: String, question: String, answer: String) {
    flashcardNumber++
    Runtime.getRuntime().exec(arrayOf(
        "convert", "-size", "240x320", "xc:black",
        "-font", "FreeMono", "-weight", "bold", "-pointsize", "24",
        "-fill", "white", "-annotate", "+12+24", "$name\n$heading\n${question.wrap(15)}",
        "-fill", "yellow", "-annotate", "+12+185", answer.replace(" : ", "\n").wrap(15),
        "%s.%03d.png".format(name, flashcardNumber)))
}
var flashcardNumber = 0

fun processStdin(name: String) {
    var heading = ""
    System.`in`.bufferedReader().lines().forEach { line ->
        if (line.startsWith("==")) {
            heading = line.drop(2).toLowerCase()
        } else if (line.isNotBlank()) {
            val i = line.indexOf(":")
            makeFlashcard(name, heading, line.take(i), line.drop(i + 1).trim())
        }
    }
}

