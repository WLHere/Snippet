package com.bwl.test

import android.os.SystemClock
import java.lang.reflect.InvocationHandler
import java.lang.reflect.Method
import java.lang.reflect.Proxy

/**
 * Created by baiwenlong on 2020/8/4
 */

fun <R> Any?.debounce(): R {
    return DebounceUtil.debounce(this)
}

fun <R> Any?.debounce(interval: Long): R {
    return DebounceUtil.debounce(this, interval)
}

object DebounceUtil {
    private const val DEFAULT_DURATION = 500L// 默认的时间

    fun <R> debounce(listener: Any?): R {
        return debounce(listener, DEFAULT_DURATION)
    }

    fun <R> debounce(listener: Any?, timeInterval: Long): R {
        if (listener == null) {
            return listener as R
        }
        val messages = listener.javaClass.interfaces
        require(!messages.isNullOrEmpty()) { "必须实现一个接口" }

        return Proxy.newProxyInstance(listener.javaClass.classLoader, messages, object :
            InvocationHandler {
            private val results = HashMap<Method, Pair<Long, Any?>>()

            @Throws(Throwable::class)
            override fun invoke(proxy: Any, method: Method, args: Array<Any>): Any? {
                var result = results[method]
                val curTime = SystemClock.elapsedRealtime()
                if (result == null || curTime - result.first > timeInterval) {
                    result = Pair(curTime, method.invoke(listener, *args))
                    results[method] = result
                }
                return result.second
            }
        }) as R
    }
}