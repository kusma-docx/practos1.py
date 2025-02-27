from library import authorize_user, main_menu

if __name__ == "__main__":
    while True:
        if authorize_user():
            main_menu()
        else:
            print("Попробуйте снова.")