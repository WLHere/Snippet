package com.example.viewflip

import android.animation.Animator
import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.view.View
import android.view.animation.AccelerateInterpolator
import android.view.animation.DecelerateInterpolator

/**
 * 翻转工具类
 * 可以通过设置android:outlineSpotShadowColor="#00000000"去掉阴影
 */
object FlipUtil {
    const val DIRECTION_LEFT_UP = 0
    const val DIRECTION_RIGHT_UP = 1

    /**
     * 垂直翻转
     */
    fun flip(frontView: View, backView: View, duration: Long, direction: Int) {
        frontView.visibility = View.VISIBLE
        backView.visibility = View.INVISIBLE

        val front1: Float
        val front2: Float
        val back1: Float
        val back2: Float
        when (direction) {
            DIRECTION_LEFT_UP -> {
                front1 = 0f
                front2 = 90f
                back1 = -90f
                back2 = 0f
            }
            DIRECTION_RIGHT_UP -> {
                front1 = 0f
                front2 = -90f
                back1 = 90f
                back2 = 0f
            }
            else -> {
                return
            }
        }
        val animatorSet = AnimatorSet()
        animatorSet.playSequentially(ObjectAnimator.ofFloat(frontView, View.ROTATION_Y, front1, front2).also {
            it.duration = duration
            it.interpolator = AccelerateInterpolator()
            it.addListener(object : Animator.AnimatorListener {
                override fun onAnimationRepeat(animation: Animator?) {
                }

                override fun onAnimationEnd(animation: Animator?) {
                    frontView.visibility = View.INVISIBLE
                }

                override fun onAnimationCancel(animation: Animator?) {
                }

                override fun onAnimationStart(animation: Animator?) {
                }
            })
        }, ObjectAnimator.ofFloat(backView, View.ROTATION_Y, back1, back2).also {
            it.duration = duration
            it.interpolator = DecelerateInterpolator()
            it.addListener(object : Animator.AnimatorListener {
                override fun onAnimationRepeat(animation: Animator?) {
                }

                override fun onAnimationEnd(animation: Animator?) {
                }

                override fun onAnimationCancel(animation: Animator?) {
                }

                override fun onAnimationStart(animation: Animator?) {
                    backView.visibility = View.VISIBLE
                }
            })
        })
        animatorSet.start()
    }
}