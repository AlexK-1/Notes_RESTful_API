from typing import Union
import sqlite3


class DataBase:
    def __init__(self, path: str):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cur = self.conn.cursor()
    
    def add_note(self, note_text: str) -> int:
        """
        Adds a note
        :param note_text: the text of the future note
        :return: id of the new note
        """
        self.cur.execute("INSERT INTO Notes (text) VALUES (?)", (note_text,))
        self.conn.commit()
        return self.cur.lastrowid
    
    def delete_note(self, note_id: int) -> None:
        """
        Deletes a note by its id
        :param note_id: note id
        :return: None
        """
        self.cur.execute("DELETE FROM Notes WHERE id = ?", (note_id,))
        return self.conn.commit()
    
    def change_note(self, note_id: int, note_text: str) -> None:
        """
        Changes the text of a note by its id
        :param note_id: note id
        :param note_text: new text of the note
        :return: None
        """
        self.cur.execute("UPDATE Notes SET text = ? WHERE id = ?", (note_text, note_id))
        return self.conn.commit()
    
    def get_note_text(self, note_id: int) -> Union[str, None]:  # I'm currently working on Windows 7, so I'm using Python 3.8.6
        """
        Returns the text of the note by its id
        :param note_id: note id
        :return: text of the note
        """
        result = self.cur.execute("SELECT text FROM Notes WHERE id = ?", (note_id,))
        try:
            return result.fetchone()[0]
        except:
            return None
    
    def get_all_notes(self) -> list:
        """
        Returns all the notes
        :return: the list of notes, each element is a tuple, includes the id of the note, the text and the date of creation of the note
        """
        result = self.cur.execute("SELECT * FROM Notes")
        return result.fetchall()
    
    def get_note_data(self, note_id: int) -> Union[tuple, None]:  # I'm currently working on Windows 7, so I'm using Python 3.8.6
        """
        Returns the note data by its id
        :param note_id: note id
        :return: data of the note
        """
        result = self.cur.execute("SELECT * FROM Notes WHERE id = ?", (note_id,))
        try:
            return result.fetchone()
        except:
            return None