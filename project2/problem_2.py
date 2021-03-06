import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    assert os.path.exists(path) is True
    assert os.path.isfile(path) is False

    results = []
    subdirectories = os.listdir(path)
    current_path = path

    for current_path in subdirectories:
        current_path = os.path.join(path, current_path)
        if os.path.isdir(current_path):
            results.extend(find_files(suffix, current_path))
        elif os.path.isfile(current_path) and current_path.endswith(suffix):
            results.append(current_path)

    return results


for dir in find_files(".c", "/Users/aliumujib/Desktop/RoadToAI/learningpython/DSandAlgos/project2/testdir"):
    print(dir)

for dir in find_files(".c", "/Users/aliumujib/Desktop/RoadToAI/learningpython/DSandAlgos/project2/testdirectory"):
    print(dir)

for dir in find_files(".c", ""):
    print(dir)
