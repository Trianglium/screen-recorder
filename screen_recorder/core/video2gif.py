from moviepy.editor import VideoFileClip

def video2gif(filename="", gifname=""):
    if filename == "":
        return "Enter a Video File to begin"

    if gifname == "":
        gifname = filename.split(".")[0] + ".gif"
    
    filename = VideoFileClip(filename)
    filename.write_gif(gifname)
    return f"Success! {filename} converted to {gifname}."

if __name__ == '__main__':
    file_input = input("File name: ")
    print(video2gif(file_input))