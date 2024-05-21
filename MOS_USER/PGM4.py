class File:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class SingleLevelDirectory:
    def __init__(self):
        self.files = {}

    def add_file(self, file):
        self.files[file.name] = file

    def search_file(self, file_name):
        if file_name in self.files:
            return self.files[file_name]
        else:
            return None

class TwoLevelDirectory:
    def __init__(self):
        self.master_directory = {}

    def add_user_directory(self, user, directory):
        self.master_directory[user] = directory

    def search_file(self, user, file_name):
        if user in self.master_directory:
            user_directory = self.master_directory[user]
            return user_directory.search_file(file_name)
        else:
            return None

class HierarchicalDirectory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

    def add_file(self, file):
        self.files[file.name] = file

    def add_subdirectory(self, directory):
        self.subdirectories[directory.name] = directory

    def search_file(self, file_name):
        if file_name in self.files:
            return self.files[file_name]
        else:
            for subdirectory in self.subdirectories.values():
                result = subdirectory.search_file(file_name)
                if result:
                    return result
            return None

if __name__ == "__main__":
    print("Single Level Directory:")
    single_level_dir = SingleLevelDirectory()
    while True:
        file_name = input("Enter file name (or 'exit' to stop adding files): ")
        if file_name.lower() == 'exit':
            break
        owner = input("Enter owner name: ")
        single_level_dir.add_file(File(file_name, owner))

    search_file_name = input("Enter file name to search: ")
    result = single_level_dir.search_file(search_file_name)
    if result:
        print(f"File found! Owner: {result.owner}")
    else:
        print("File not found!")

    print("\nTwo Level Directory:")
    two_level_dir = TwoLevelDirectory()
    while True:
        user = input("Enter user name (or 'exit' to stop adding users): ")
        if user.lower() == 'exit':
            break
        user_dir = SingleLevelDirectory()
        while True:
            file_name = input(f"Enter file name for user '{user}' (or 'exit' to stop adding files for this user): ")
            if file_name.lower() == 'exit':
                break
            user_dir.add_file(File(file_name, user))
        two_level_dir.add_user_directory(user, user_dir)

    user_name = input("Enter user name to search: ")
    file_name = input("Enter file name to search: ")
    result = two_level_dir.search_file(user_name, file_name)
    if result:
        print(f"File found! Owner: {result.owner}")
    else:
        print("File not found!")

    print("\nHierarchical Directory:")
    root_dir = HierarchicalDirectory("root")
    while True:
        directory_name = input("Enter directory name (or 'exit' to stop adding directories): ")
        if directory_name.lower() == 'exit':
            break
        directory = HierarchicalDirectory(directory_name)
        while True:
            file_name = input(f"Enter file name for directory '{directory_name}' (or 'exit' to stop adding files for this directory): ")
            if file_name.lower() == 'exit':
                break
            owner = input("Enter owner name: ")
            directory.add_file(File(file_name, owner))
        root_dir.add_subdirectory(directory)

    search_file_name = input("Enter file name to search: ")
    result = root_dir.search_file(search_file_name)
    if result:
        print(f"File found! Owner: {result.owner}")
    else:
        print("File not found!")
