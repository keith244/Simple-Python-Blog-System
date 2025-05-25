import time
from datetime import datetime
class User:

    def __init__(self,username):
        self.username = username

class BlogPost:
    blog_list = []
    def __init__(self,user,title='',body=''):
        self.title = title
        self.body = body
        self.user = user
    

    def user_action(self,):
        while True:
            user_choice = input('\nWhat would you like to do?\n1. Create Post\n2. Read posts\n3. Delete post\n4. Exit\nYour choice: ')
            
            if user_choice == '1':
                self.create_post()
            elif user_choice == '2':
                self.show_posts()
            elif user_choice == '3':
                self.delete_post()
            elif user_choice == '4' or user_choice.lower() in ['exit', 'quit']:
                print('Exiting the blog program. Goodbye!')
                break
            else:
                print('Invalid choice. Try again!')

    
    def create_post(self,):
        title = str(input('Enter blog title: ')).strip()
        body = str(input('Body : ')).strip()

        if title and body:
            for i in range(3):
                print('Posting...')
                time.sleep(0.5)
            new_post = BlogPost(self.user, title, body)
            BlogPost.blog_list.append(new_post)
            print(f"Post: '{title}' created successfully!")

        else:
            print('Error: Both title and body are required.')


    def show_posts(self):
        if not BlogPost.blog_list:
            print('No posts to show.')
            print("Press Y to add the first post")
            choice = input('Enter Y to add new post or N to cancel: ').lower()
            if choice == 'y':
                self.create_post()
            else:
                return
            return 
        print()
        print("\n==== ALL POSTS ====")
        for i,blog in enumerate(BlogPost.blog_list, start=1):
            print(f'Post {i}:\n{blog.user.username}: \n{blog}')
        print()
        print("\n==== END ====")
        print()

    
    def delete_post(self,):
        if not BlogPost.blog_list:
            print('No posts to delete.')
            return 
        
        print('\nAvailable Posts:')
        for i, blog in enumerate(BlogPost.blog_list,1):
            print(f'{i}. {blog.title} (by {blog.user.username})')
        try:
            index = int(input('\nEnter post number to delete (0 to cancel): ')) -1

            if index == -1:
                print('Deletion canceled.')
                return
            if 0 <=index < len (BlogPost.blog_list):
                removed = BlogPost.blog_list.pop(index)
                print(f'Deleted Post: {removed.title}')
            else:
                print('Invalid post number')
        except ValueError:
            print('Please enter a valid number.')

             
    def __str__(self):
        return f"--- {self.title.upper()} ---\nAuthor: {self.user.username}\n{self.body}\n"

def main():
    print('Welcome to My Blog App!')
    username = input('Enter your username: ')
    current_user = User(username)

    blog = BlogPost(current_user)

    blog.user_action()

if __name__ == "__main__":
    main()



# post = BlogPost()
# post.create_post()

# another = BlogPost()
# another.create_post()

# post.show_posts()