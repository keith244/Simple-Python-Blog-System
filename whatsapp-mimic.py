import time
from datetime import datetime

class User:
    def __init__(self,username):
        self.username = username

class Group:
    created_at = datetime.now().strftime('%H:%M:%S')
    groups = []

    def __init__(self,user,name='',description='', ):
        self.user = user
        self.name = name
        self.description = description
    
    def create_group(self):
        name = input('Enter name of group: ').strip()
        description = input('Enter group description: ').strip()

        if name and description:
            self.name = name
            self.description = description
            # new_group = Group(self.user, name, description)
            Group.groups.append(self)
            print(f"Group: '{name}' created successfully!")

        else:
            print('Error: Both name and description are required.')
    
    def show_groups(self):
        if not self.groups:
            print('No groups created.')
            return 
        print(f"\n==== {self.name} MEMBERS ====")
        for i,group in enumerate(Group.groups, start=1):
            print(f'{group.name} => created by {group.user.username}')   
        print()
        print("\n==== END ====")
    
    def delete_groups(self):
        if not Group.groups:
            print('No groups available.Exiting...')
            return
        for i, group in enumerate(Group.groups,start=1):
            print(f'{i}. {group.name} ( {group.user.username})')
        try:
            while True:
                index = int(input('\nEnter group number to delete (0 to cancel): ')) -1

                if index == -1:
                    print('Deletion canceled.')
                    break
                if 0 <=index < len (Group.groups):
                    selected_group = Group.groups[index]
                    if selected_group.user.username != self.user.username:
                        print('You cannot delete a group you didn\'t create.')
                        return
                    deleted = Group.groups.pop(index)
                    print(f'Removed: {deleted.name}')
                    break
                else:
                    print('Invalid number')
        except ValueError:
            print('Please enter a valid number.')

    def __str__(self):
        return f"--- {self.name.upper()} created at: {Group.created_at}---\nCreator: {self.user.username}\n{self.description}\n"

class GroupManagement:

    def __init__(self,group):
        self.group = group
        self.group_members = []
        self.member_roles = {}
        self.group_members.append(group.user)
        self.member_roles[group.user.username] = 'Admin'

    def add_member(self,user):
        try:
            while True:
                username = input('Enter new member username (or type "quit" to exit) ').strip().lower()
                if username == 'quit':
                    break
                if username not in self.member_roles:
                    new_user = User(username)
                    self.group_members.append(new_user)
                    self.member_roles[username] = 'member'
                    print(f'{username} added to {self.group.name}.')
                else:
                    print(f'{username} is already in the group.')
        except Exception as e:
            print(f'Unable to add member: {e}')
    
    def remove_member(self,):
            # username = self.member_roles[username]
            if not self.group_members:
                print('No members.')
            for i, member in enumerate(self.group_members,1):
                role = self.member_roles[member.username]
                print(f'{i}. {member.username} ( {role})')
            try:
                while True:
                    index = int(input('\nEnter member number to remove (0 to cancel): ')) -1

                    if index == -1:
                        print('Remove canceled.')
                        break
                    if 0 <=index < len (self.group_members):
                        selected_member = self.group_members[index]
                        if self.member_roles[selected_member.username] == 'Admin':
                            print('Cannot remove admin!')
                            return
                        removed = self.group_members.pop(index)
                        print(f'Removed: {removed.username}')
                    else:
                        print('Invalid number')
            except ValueError:
                print('Please enter a valid number.')

    def show_members_and_roles(self):
        # user = User()
        # try:
        if not self.group:
            print('No groups created.')
            return 
        print(f"\n==== {self.group.name} MEMBERS ====")
        for i,member in enumerate(self.group_members, start=1):
            role = 'Admin' if member.username == self.group.user.username else 'member'
            print(f'{member.username} => {role}')   
        print()
        print("\n==== END ====")
            
    def __str__(self):
        return f'{self.group.name} by {self.group.user.username}'
    
def main():
    username = input("Enter your username: ").strip()
    if not username:
        print("Username is required.")
        return

    user = User(username)
    group_instance = Group(user)

    while True:
        print("\n=== MENU ===")
        print("1. Create Group")
        print("2. Show Groups")
        print("3. Delete Group")
        print("4. Manage Group")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            group_instance.create_group()

        elif choice == "2":
            group_instance.show_groups()

        elif choice == "3":
            group_instance.delete_groups()

        elif choice == "4":
            if not Group.groups:
                print("No groups to manage.")
                continue

            print("\nSelect a group to manage:")
            for i, g in enumerate(Group.groups, start=1):
                print(f"{i}. {g.name} (created by {g.user.username})")

            try:
                index = int(input("Enter number: ")) - 1
                if 0 <= index < len(Group.groups):
                    selected_group = Group.groups[index]
                    if selected_group.user.username != user.username:
                        print("You can only manage your own groups.")
                        continue

                    manager = GroupManagement(selected_group)

                    while True:
                        print("\n--- Manage Menu ---")
                        print("1. Add Member")
                        print("2. Remove Member")
                        print("3. Show Members")
                        print("4. Back")

                        action = input("Select action: ").strip()

                        if action == "1":
                            manager.add_member(user)
                        elif action == "2":
                            manager.remove_member()
                        elif action == "3":
                            manager.show_members_and_roles()
                        elif action == "4":
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()