from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import moviepy.video.fx.all as vfx

def speedup_with_label(input_path, output_path, speed=2.0):
    clip = VideoFileClip(input_path)

    # 2倍速
    clip_fast = clip.fx(vfx.speedx, speed)

    # 左下角 label
    txt = (
        TextClip(f"{int(speed)}X", fontsize=50, color='white', font='Arial-Bold')
        .set_position(("left", "bottom"))
        .set_duration(clip_fast.duration)
    )

    final = CompositeVideoClip([clip_fast, txt])
    final.write_videofile(output_path, codec='libx264', fps=clip.fps)

if __name__ == "__main__":
    speedup_with_label(
        input_path="/Users/aureleo/科研Embodied/研一上/DexVLA/demo/pick_place_the_apple2.mp4",
        output_path="/Users/aureleo/科研Embodied/研一上/DexVLA/demo/process_demo/pick_place_the_apple2.mp4",
        speed=2.0
    )
