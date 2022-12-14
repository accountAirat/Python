import txt_reader
import txt_writer
import csv_writer


def TxtTxt():
    txt_writer.write(txt_reader.read())


def TxtCsv():
    csv_writer.write(txt_reader.read())
