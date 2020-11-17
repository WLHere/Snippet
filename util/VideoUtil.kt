/**
 * 视频工具类
 */
object VideoUtil {
    
    /**
     * 返回centerCrop的matrix
     */
    fun createCenterCropMatrix(viewWidth: Int, viewHeight: Int, videoWidth: Int, videoHeight: Int): Matrix {
        val sx = viewWidth.toFloat() / videoWidth
        val sy = viewHeight.toFloat() / videoHeight
        val matrix = Matrix()
        val maxScale = sx.coerceAtLeast(sy)

        //第1步:把视频区移动到View区,使两者中心点重合.
        matrix.preTranslate((viewWidth - videoWidth) / 2.toFloat(), (viewHeight - videoHeight) / 2.toFloat())

        //第2步:因为默认视频是fitXY的形式显示的,所以首先要缩放还原回来.
        matrix.preScale(videoWidth / viewWidth.toFloat(), videoHeight / viewHeight.toFloat())

        //第3步,等比例放大或缩小,直到视频区的一边超过View一边, 另一边与View的另一边相等. 因为超过的部分超出了View的范围,所以是不会显示的,相当于裁剪了.
        matrix.postScale(maxScale, maxScale, viewWidth / 2.toFloat(), viewHeight / 2.toFloat()) //后两个参数坐标是以整个View的坐标系以参考的
        return matrix
    }
}
