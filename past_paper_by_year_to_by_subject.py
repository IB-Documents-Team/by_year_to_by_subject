import shutil
import re
import os
import sys

"""
Written originally by batmansmaster, intended to be run by TemplarKnight98.
Modifications by TemplarKnight98 and pants.
"""

# Start Config

dir_source = "by_year"
dir_destination = "by_subject"
normal_pattern = r"(\d{4}).*(May|November) \1 Examination Session\\*((Group \d) - )?" \
                 r"(.*)[\\](.*)(_|__)paper(_|__)(\d)(.*)"
audio_music_pattern = r"(\d{4}).*(May|November) \1 Examination Session\\*((Group \d) - )?(.*)[\\](.*)"

# End Config

abs_working_directory = os.path.dirname(os.path.realpath(__file__))
abs_source_directory = os.path.join(abs_working_directory, dir_source)
abs_destination_directory = os.path.join(abs_working_directory, dir_destination)

normal_regex = re.compile(normal_pattern)
audio_music_regex = re.compile(audio_music_pattern)


def format_group_name(gn):
    """
    A sort of switch-statement to convert incorrect (new) to correct (old) group names to ensure consistency.
    :param gn: The incorrect group name
    :return: The correct group name
    """

    return {
        "Studies in language and literature": "Group 1 - Studies in Language and Literature",
        "Language acquisition": "Group 2 - Language Acquisition",
        "Individuals and societies": "Group 3 - Individuals and Societies",
        "Experimental sciences": "Group 4 - Sciences",
        "Mathematics": "Group 5 - Mathematics",
        "The arts": "Group 6 - The Arts"
    }[gn]


def write_copy(file_source_path, original_file_name, **kwargs):
    """
    Writes files to the output directory based off of input parameters.
    :param file_source_path: The source file path.
    :param original_file_name: The name of the source original file.
    :param kwargs: Expects:
      (OPTIONALLY) matched_groups, fake_difficulty
    """

    group_dir, subject_dir, year_session_dir = None, None, None

    matched_groups = kwargs.get("matched_groups")
    if matched_groups is not None:
        """
        matched_groups[0] = year
        matched_groups[1] = session
        matched_groups[2] = subject group number with hyphen (if applicable)
        matched_groups[3] = subject group number (if applicable)
        matched_groups[4] = subject group name
        matched_groups[5] = subject name
        matched_groups[8] = paper number
        matched_groups[9] = further info
        """

        # Handling computer science's change of group
        if "Computer_science" in matched_groups[5] and "Mathematics" in matched_groups[4]:
            group_dir = "Group 4 - Sciences"
        # Continuing regular group handing
        elif matched_groups[3] is None:
            group_dir = format_group_name(matched_groups[4])
        else:
            group_dir = matched_groups[2] + matched_groups[4]

        # Handling difficulty. Bulk of it is handling HLSL files and files with no difficulty stated.
        fake_difficulty = kwargs.get("fake_difficulty")
        if fake_difficulty is not None:
            difficulty = fake_difficulty
        elif "HLSL" in original_file_name:
            write_copy(file_source_path, original_file_name, matched_groups=matched_groups, fake_difficulty="HL")
            write_copy(file_source_path, original_file_name, matched_groups=matched_groups, fake_difficulty="SL")
            return
        elif "HL" in original_file_name:
            difficulty = "HL"
        elif "SL" in original_file_name:
            difficulty = "SL"
        else:
            write_copy(file_source_path, original_file_name, matched_groups=matched_groups, fake_difficulty="HL")
            write_copy(file_source_path, original_file_name, matched_groups=matched_groups, fake_difficulty="SL")
            return

        # This is where we handle deprecated/changed subject names
        subject = matched_groups[5]
        if "Business_and_management" in subject:
            subject = subject.replace("Business_and_management", "Business_management")
        elif "Belarussian" in subject:
            subject = subject.replace("Belarussian", "Belarusian")
        elif "Biology_HL" in subject:
            subject = subject.replace("Biology_HL", "Biology")
        elif "Biology_SL" in subject:
            subject = subject.replace("Biology_SL", "Biology")
        elif "Ecosystems_and_societies_SL" in subject:
            subject = subject.replace("Ecosystems_and_societies_SL", "Ecosystems_and_societies")
        elif "Environmental_systems_SL" in subject:
            subject = subject.replace("Environmental_systems_SL", "Environmental_systems")
        elif "History_route_1" in subject:
            subject = subject.replace("History_route_1", "History")
        elif "History_route_2" in subject:
            subject = subject.replace("History_route_2", "History")
        elif "History_of_the_Islamic_World" in subject:
            subject = subject.replace("History_of_the_Islamic_World", "Islamic_history")

        subject_dir = f"{subject}_{difficulty}"
        year_session_dir = f"{matched_groups[0]} {matched_groups[1]} Examination Session"

    music_groups = kwargs.get("music_groups")
    if music_groups is not None:
        """
        music_groups[0] = year
        music_groups[1] = session
        music_groups[2] = subject group number with hyphen (if applicable)
        music_groups[3] = subject group number (if applicable)
        music_groups[4] = subject group name
        music_groups[5] = file name
        """

        group_dir = "Group 6 - The Arts"
        subject = "Music"

        # Handling difficulty. Bulk of it is handling HLSL files and files with no difficulty stated.
        fake_difficulty = kwargs.get("fake_difficulty")
        if fake_difficulty is not None:
            difficulty = fake_difficulty
        elif "HLSL" in original_file_name:
            write_copy(file_source_path, original_file_name, music_groups=music_groups, fake_difficulty="HL")
            write_copy(file_source_path, original_file_name, music_groups=music_groups, fake_difficulty="SL")
            return
        elif "HL" in original_file_name:
            difficulty = "HL"
        elif "SL" in original_file_name:
            difficulty = "SL"
        else:
            write_copy(file_source_path, original_file_name, music_groups=music_groups, fake_difficulty="HL")
            write_copy(file_source_path, original_file_name, music_groups=music_groups, fake_difficulty="SL")
            return

        subject_dir = f"{subject}_{difficulty}"
        year_session_dir = f"{music_groups[0]} {music_groups[1]} Examination Session"

    audio_groups = kwargs.get("audio_groups")
    if audio_groups is not None:
        """
        audio_groups[0] = year
        audio_groups[1] = session
        audio_groups[2] = subject group number with hyphen (if applicable)
        audio_groups[3] = subject group number (if applicable)
        audio_groups[4] = subject group name (contains '\\audio' in some instances)
        audio_groups[5] = file name
        """

        group_dir = "Group 6 - The Arts"

        fake_difficulty = kwargs.get("fake_difficulty")
        if fake_difficulty is not None:
            difficulty = fake_difficulty
        else:
            write_copy(file_source_path, original_file_name, audio_groups=audio_groups, fake_difficulty="HL")
            write_copy(file_source_path, original_file_name, audio_groups=audio_groups, fake_difficulty="SL")
            return

        subject_dir = f"Music_{difficulty}"
        year_session_dir = f"{audio_groups[0]} {audio_groups[1]} Examination Session"
        year_session_dir = os.path.join(year_session_dir, "audio")

    if None not in [group_dir, subject_dir, year_session_dir]:
        new_filepath = os.path.join(abs_destination_directory, group_dir, subject_dir, year_session_dir,
                                    original_file_name)
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
        shutil.copy(file_source_path, new_filepath)
    else:
        print(f"CRITICAL ERROR: File  had 'None' path attributes: {file_source_path}")


def start():
    """
    Iterates over every file in source_dir in order to re-organise based off of pre-defined regex into a by-subject
      structure.
    """

    total_files = sum([len(files) for r, d, files in os.walk(abs_source_directory)])
    total_files_down = total_files
    for i in range(total_files, 0, -1):
        if i % 10 == 0:
            total_files_down = i
            break
    current_iteration = 0
    last_factor = 0
    position = 1
    print("[{0}] {1}/{2}".format(" " * 10, 0, total_files))
    for path, dirs, files in os.walk(abs_source_directory):
        for file_name in list(filter(lambda x: x.endswith(".pdf"), files)):
            file_source_path = os.path.join(path, file_name)
            out = re.search(normal_regex, file_source_path)
            # Handles normal past-papers
            try:
                found_groups = out.groups()
                write_copy(file_source_path, file_name, matched_groups=found_groups)
            except AttributeError:
                # Handles music past-papers
                if "Music_" in file_source_path:
                    out = re.search(audio_music_regex, file_source_path)
                    try:
                        found_groups = out.groups()
                        write_copy(file_source_path, file_name, music_groups=found_groups)
                    except AttributeError:
                        print(f"CRITICAL ERROR: File not handled: {file_source_path}")
                elif "Exam Pack list of omitted papers and markschemes" in file_name:
                    pass
                else:
                    print(f"CRITICAL ERROR: File not handled: {file_source_path}")
            current_iteration += 1
            if current_iteration == last_factor + total_files_down / 10:
                last_factor = current_iteration
                print("[{0}{1}] {2}/{3}".format("-" * position, " " * (10 - position), current_iteration, total_files))
                position += 1
        # Handles mp3 files
        for file_name in list(filter(lambda x: x.endswith(".mp3"), files)):
            file_source_path = os.path.join(path, file_name)
            out = re.search(audio_music_regex, file_source_path)
            try:
                found_groups = out.groups()
                write_copy(file_source_path, file_name, audio_groups=found_groups)
            except AttributeError:
                print(f"CRITICAL ERROR: File not handled: {file_source_path}")
            current_iteration += 1
            if current_iteration == last_factor + total_files_down / 10:
                last_factor = current_iteration
                print("[{0}{1}] {2}/{3}".format("-" * position, " " * (10 - position), current_iteration, total_files))
                position += 1
    print("[{0}] {1}/{2}".format("-" * 10, total_files, total_files))


start()
print("Done.")
