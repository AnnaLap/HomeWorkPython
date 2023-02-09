import view
import model


def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book, user_choice)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                id = view.get_id(phone_book)
                new_line = list(view.new_contact())
                model.edit_contact(id, new_line)
            case 6:
                id = view.get_id(phone_book)
                model.delete_contact(id)
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result, user_choice)
    if user_choice == 8:
        if model.get_difference() == 1:
            exit = view.saving_choice()
            if exit == 1:
                model.save_phone_book()
                view.save_success()
        return ()
