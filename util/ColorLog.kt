package com.wlhere.defer.base

/**
 * Created by baiwenlong on 12/22/20.
 */
object ColorLog {
    const val ANSI_RESET = "\u001B[0m"
    const val ANSI_BLACK = "\u001B[30m"
    const val ANSI_RED = "\u001B[31m"
    const val ANSI_GREEN = "\u001B[32m"
    const val ANSI_YELLOW = "\u001B[33m"
    const val ANSI_BLUE = "\u001B[34m"
    const val ANSI_PURPLE = "\u001B[35m"
    const val ANSI_CYAN = "\u001B[36m"
    const val ANSI_WHITE = "\u001B[37m"

    fun debug(log: String?) {
        println(log)
    }

    fun info(log: String?) {
        println("$ANSI_GREEN$log$ANSI_RESET")
    }

    fun warn(log: String?) {
        println("$ANSI_YELLOW$log$ANSI_RESET")
    }

    fun error(log: String?) {
        println("$ANSI_RED$log$ANSI_RESET")
    }
}