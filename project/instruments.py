import requests
from project.data import documents, directories


# Class of all commands
class SecretaryApp:
    def __init__(self, doc: list, dir_: dict):
        self.doc = doc
        self.dir = dir_

    # "P"
    def get_doc_owner_name(self, doc_num: str):
        for elem in self.doc:
            if elem['number'] == doc_num:
                return elem['name']
        print('Doc num does not exist')
        return None

    # "S"
    def get_doc_shelf_num(self, doc_num: str):
        for k, v in self.dir.items():
            if doc_num in v:
                return k
        print('Doc num does not exist')
        return None

    # "L"
    def get_all_doc(self) -> list:
        return [f'{elem["type"]} "{elem["number"]}" "{elem["name"]}"' for elem in self.doc]

    # "A"
    def add_new_doc(self, type_doc: str, num_doc: str, name: str, to_dir: str):
        if to_dir not in self.dir:
            print('Shelf num does not exist')
            return False
        self.doc.append({"type": type_doc, "number": num_doc, "name": name})
        self.dir[to_dir].append(num_doc)
        return True

    # "D"
    def del_doc(self, doc_num: str):
        if self.get_doc_owner_name(doc_num) is None or self.get_doc_shelf_num(doc_num) is None:
            return False
        else:
            for elem in range(len(self.doc)):
                if self.doc[elem]['number'] == doc_num:
                    self.doc.remove(self.doc[elem])
                    break
            self.dir[self.get_doc_shelf_num(doc_num)].remove(doc_num)
        return True

    # "M"
    def move_doc_shelf(self, doc_num, to_shelf_num):
        if self.get_doc_shelf_num(doc_num) is None:
            return False
        elif to_shelf_num not in self.dir:
            print('Shelf num does not exist')
            return False
        find_index = self.dir[self.get_doc_shelf_num(doc_num)].index(doc_num)
        pop_item = self.dir[self.get_doc_shelf_num(doc_num)].pop(find_index)
        self.dir[to_shelf_num].append(pop_item)
        return True

    # "AS"
    def add_new_shelf(self, new_shelf_num: str):
        if new_shelf_num in self.dir:
            print('Shelf already exist')
            return False
        else:
            if new_shelf_num.isdigit():
                self.dir[new_shelf_num] = []
            else:
                print('Shelf num should be only digit')
                return False
        return True

    def __del__(self):
        print('object deleted')


# Yandex Func to Create New Folder
def create_new_folder_ya_disk(token, folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(url=url, headers=headers, params={'path': f'{folder_name}'})
    return response.status_code


if __name__ == '__main__':
    s = SecretaryApp(documents, directories)
    print(s.get_all_doc())
