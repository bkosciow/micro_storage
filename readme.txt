Helper for managing app data.
Two engines:
- dictionary - non persistent
- sqlite - persistent


from micro_storage.storage import Storage
from micro_storage.dictionary_engine import DictionaryEngine
from micro_storage.sqlite_engine import SQLiteEngine

Storage.set_engine(DictionaryEngine())
storage = Storage()


Storage.set_engine(SQLiteEngine())
storage = Storage()


    set(key, value)
    get(key)
    exists(key)


Events propagated on set and get

storage.on('set', self.handle_new_data)
