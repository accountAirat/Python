import model
import view


form = ['id','surname','name','patronymic','position','salary','phone','phone_2','phone_3']
position = ['Менеджер','Программист','Директор']

def сall_action():
    temp_data = []
    selector = -1
    while selector != 0:
        selector = view.show_menu()
        data = model.read_txt(form)
        match selector:
            case 1:
                selector_2 = -1
                while selector_2 != 0:
                    view.print_list(temp_data)
                    selector_2 = view.parameter_search_worker()
                    match selector_2:
                        case 1:
                            value = view.input_value()
                            temp_data = model.search_worker(data, form[1] , value)
                        case 2:
                            value = view.input_value()
                            temp_data = model.search_worker(data, form[2] , value)
                        case 3:
                            value = view.input_value()
                            temp_data = model.search_worker(data, form[3] , value)
                        case 4:
                            value = view.input_value()
                            temp_data = model.search_worker(data, form[0] , value)
                        case 0:
                            view.exit()
            case 2:
                selector_2 = -1
                while selector_2 != 0:
                    view.print_list(temp_data)
                    selector_2 = view.position_selection()
                    match selector_2:
                        case 1:
                            temp_data = (model.search_worker(data, form[4], position[0]))
                        case 2:
                            temp_data = (model.search_worker(data, form[4], position[1]))
                        case 3:
                            temp_data = (model.search_worker(data, form[4], position[2]))
                        case 0:
                            view.exit()
            case 3:
                temp_data = model.search_salary(data,form[5],view.salary_range())
                view.print_list(temp_data)
            case 4:
                data = model.add_worker(data, form, view.input_full_name())
                model.write_txt(data)
            # case 5:
            #     delete_worker(data)
            # case 6:
            #     update_worker_data(data)
            # case 7:
            #     json_export(data)
            # case 8:
            #     cmv_export(data)  
    view.exit()
