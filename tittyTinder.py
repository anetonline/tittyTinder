#Python2 code for mystic
#StingRay - A-Net Online BBSs
import pickle
import random
import bisect
import itertools
import os
import mystic_bbs as bbs

def display_image(image_name):
    try:
        with open(image_name, "rb") as file:
            content = file.read().decode('utf-8', 'replace').replace('\x00', '')
            bbs.write(content)
    except IOError:
        bbs.write("Error: '{}' not found\n".format(image_name))

def get_user_input(prompt):
    bbs.write(prompt)
    input_str = bbs.getstr(1, 1, 1, "")
    if input_str is None:
        return ""
    return input_str.upper()

def get_user_input_with_arrows(prompt):
    bbs.write(prompt)
    input_str = bbs.getstr(10, 1, 1, "")
    if input_str is None:
        return ""
    bbs.write("Debug: input_str = '{}'\n".format(input_str))  # Debugging line
    if input_str in ["\x1b[C", "R", "r"]:
        return 'R'
    if input_str in ["\x1b[D", "L", "l"]:
        return 'L'
    return input_str.upper()

def vote_for_images(image_names):
    votes = {image: 0 for image in image_names}
    index = 0

    while index < len(image_names):
        display_image(image_names[index])
        key = get_user_input_with_arrows("\nSwipe left (L) to skip or right (R) to vote for this image.\n")
        bbs.write("Debug: key = '{}'\n".format(key))  # Debugging line
        if key == 'R':
            votes[image_names[index]] += 1
        if key in ['L', 'R']:
            index += 1

    sorted_images = sorted(votes.items(), key=lambda item: item[1], reverse=True)
    for image, vote_count in sorted_images:
        bbs.write("\nVotes: {}\n".format(vote_count))
        display_image(image)

def main():
    user = bbs.getuser(0)
    player_handle = user["handle"]

    # List of ANSI image files to display
    image_names = ["/home/jerry/mystic/tt/1.ans", "/home/jerry/mystic/tt/2.ans", "/home/jerry/mystic/tt/3.ans", "/home/jerry/mystic/tt/4.ans"]
    vote_for_images(image_names)
    bbs.write("\nVoting complete. Exiting...\n")

if __name__ == "__main__":
    main()
