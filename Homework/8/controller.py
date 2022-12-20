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
                model.write_txt(model.add_worker(data, form, view.input_worker_data()))
            case 5:
                model.write_txt(model.delete_worker(data, form[0], view.input_id()))
            case 6:
                id = view.input_id()
                temp = view.input_worker_data()
                model.delete_worker(data, form[0],id)
                model.write_txt(model.update_worker(data, form, temp, id))               
            case 7:
                model.write_json(data)
            case 8:
                model.write_csv(data,form)  
    view.exit()
