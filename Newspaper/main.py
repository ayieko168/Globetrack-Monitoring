from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from utils import main_design_ui


import os
import datetime
import json
#from fpdf import FPDF
from PIL import Image
import re
import subprocess

class MainApplication(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = main_design_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        ## Variables
        self.to_send_emails = []
        self.threadpool = QThreadPool()

        ## Setup Functions
        self.ui_connections()
        self.initialize_ui()

    def initialize_ui(self):

        ## Clear all fields
        self.ui.paper_dir_edit.clear()
        self.ui.output_file_edit.clear()
        self.ui.mail_list_listwidget.clear()
        self.ui.teo_send_listwidget.clear()
        self.ui.output_log_textedit.clear()

        ## Populate existing emails
        with open("utils/config.json") as conf_fo:
            data = json.load(conf_fo)
            emails_data = data['Emails']
            self.ui.mail_list_listwidget.addItems(emails_data)


    def ui_connections(self):

        self.ui.paper_dir_search_button.clicked.connect(self.search_paper_dir)
        self.ui.output_file_search_button.clicked.connect(self.search_output_file)
        self.ui.add_mail_to_listing_button.clicked.connect(self.add_mail_to_listing)
        self.ui.delete_mail_from_listing_button.clicked.connect(self.delete_mail_from_listing)
        self.ui.move_mails_into_send_list_button.clicked.connect(self.move_mails_into_send_list)
        self.ui.move_mails_from_send_list_button.clicked.connect(self.move_mails_from_send_list)
        self.ui.clear_send_list_button.clicked.connect(self.clear_send_list)
        self.ui.start_ops_button.clicked.connect(self.start_op_caller)


    def logger_print(self, message: str, sender='APPLICATION'):

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_text = f">[{current_time}] [{sender}] ==> {message.title()}\n"

        print(log_text)
        self.ui.output_log_textedit.moveCursor(QTextCursor.End)
        self.ui.output_log_textedit.insertPlainText(log_text)

    def search_paper_dir(self):

        file_name = QFileDialog.getExistingDirectory(directory=f"C:/Users/{os.getlogin()}/Downloads")

        ## Verify the file Name:
        if file_name.strip() == '':
            self.logger_print("Please enter a valid paper directory.")
            pass

        self.ui.paper_dir_edit.setText(file_name)

    def search_output_file(self):

        file_name, _ = QFileDialog.getSaveFileName(directory=f"C:/Users/{os.getlogin()}/Desktop",
                                                   filter="PDF File (*.pdf)")

        ## Verify the file Name:
        if file_name.strip() == '':
            self.logger_print("Please enter a valid paper directory.")
            pass

        self.ui.output_file_edit.setText(file_name)

    def add_mail_to_listing(self):

        inp = QInputDialog.getText(self, "Enter the new Email address you want to add to the list", "Email Address: ")

        if inp[0].strip() == '':
            self.logger_print("Enter a valid email address")
            return

        ## Add the email adrress to the config file
        with open("utils/config.json") as conf_fo:
            data = json.load(conf_fo)
            emails_data = data['Emails']

        emails_data.append(inp[0].lower())

        ## Update the list
        self.ui.mail_list_listwidget.clear()
        self.ui.mail_list_listwidget.addItems(emails_data)

        ## Finally write the new list to the config file
        with open("utils/config.json", 'w') as conf_fo:
            json.dump(data, conf_fo, indent=2)
            self.logger_print(f"Successfully added new email to listing > {inp[0].lower()}")

    def delete_mail_from_listing(self):

        ## verify item is selected
        if self.ui.mail_list_listwidget.currentItem() is None:
            self.logger_print("Select at least one item from the list before proceeding")
            return

        ## Get the selected item to remove
        current_item_text = self.ui.mail_list_listwidget.currentItem().text()
        current_item_index = self.ui.mail_list_listwidget.currentIndex().row()

        ## Remove the item from config file
        with open("utils/config.json") as conf_fo:
            data: dict = json.load(conf_fo)
            emails_data: list = data['Emails']
            emails_data.remove(current_item_text)
            print(data)
            with open("utils/config.json", 'w') as conf_fow:
                json.dump(data, conf_fow, indent=2)
                self.logger_print(f"Successfully removed email from listing > {current_item_text}")

        self.ui.mail_list_listwidget.takeItem(current_item_index)

        ## Re-list available emails
        with open("utils/config.json") as conf_fo:
            data = json.load(conf_fo)
            emails_data = data['Emails']
            self.ui.mail_list_listwidget.clear()
            self.ui.mail_list_listwidget.addItems(emails_data)

    def move_mails_into_send_list(self):

        ## verify item is selected
        if self.ui.mail_list_listwidget.currentItem() is None:
            self.logger_print("Select at least one item from the list before proceeding")
            return

        ## Get currently selected email
        current_item_text = self.ui.mail_list_listwidget.currentItem().text()
        current_item_index = self.ui.mail_list_listwidget.currentIndex().row()

        ## Get the current list of to send
        to_send_list = [self.ui.teo_send_listwidget.item(i).text().lower() for i in range(self.ui.teo_send_listwidget.count())]

        ## Append the selected email to the to send list
        self.to_send_emails.append(current_item_text)
        self.to_send_emails = self.to_send_emails + to_send_list

        ## Clear any duplicated
        self.to_send_emails = list(set(self.to_send_emails))

        ## populate new list
        self.ui.teo_send_listwidget.clear()
        self.ui.teo_send_listwidget.addItems(self.to_send_emails)

    def move_mails_from_send_list(self):

        ## verify item is selected
        if self.ui.teo_send_listwidget.currentItem() is None:
            self.logger_print("Select at least one item from the list before proceeding")
            return

        ## Get currently selected email
        current_item_text = self.ui.teo_send_listwidget.currentItem().text()
        current_item_index = self.ui.teo_send_listwidget.currentIndex().row()

        ## Get the current list of to send
        to_send_list = [self.ui.teo_send_listwidget.item(i).text().lower() for i in range(self.ui.teo_send_listwidget.count())]

        ## Remove selected from list
        to_send_list.remove(current_item_text)

        ## Update the listwidget with new list
        self.ui.teo_send_listwidget.clear()
        self.ui.teo_send_listwidget.addItems(to_send_list)

        ## Re-list the main email list
        self.to_send_emails = to_send_list
        self.logger_print(f"Successfully removed {current_item_text} from the emails list")

    def clear_send_list(self):

        ## Clear the listwidget
        self.ui.teo_send_listwidget.clear()

        ## Also clear the main send list
        self.to_send_emails = []

        ## Message
        self.logger_print("Cleared all emails from queue")

    def start_op_caller(self):
        
        worker = Worker(self.start_ops)
        # worker1.signals.message_signal.connect(self.backend_utils.show_messagebox)
        worker.signals.log_data.connect(self.logger_print)
        worker.signals.finished.connect(self.start_op_finished)
        self.threadpool.start(worker)

    def start_op_finished(self):
        
        print("Finished all signal ops.")

    def start_ops(self, signals):

        ## Verify the two dirs are selected
        if (not self.ui.paper_dir_edit.text()) or (not self.ui.output_file_edit.text()):
            signals.log_data.emit("Select a Newspaper directory and an output file to proceed.")
            return

        ## verify main emails list is not empty
        if not self.to_send_emails:
            signals.log_data.emit("No emails selected... Just saving the PDF...")

        ## Parse directory for paper images
        selected_paper_dir = self.ui.paper_dir_edit.text()
        files = [os.path.join(self.ui.paper_dir_edit.text(), _file) for _file in os.listdir(selected_paper_dir) if os.path.splitext(_file)[-1] == '.jpg']

        ## Sort the files
        files.sort(key=lambda f: int(re.sub('\D', '', f)))

        ## Start The PDF convertion
        print(files)
        image_objs = []
        for image in files:
            signals.log_data.emit(f"Processing {image}")
            img = Image.open(image)
            img.convert("RGB")
            image_objs.append(img)

        image_objs[0].save(self.ui.output_file_edit.text(), "PDF", resolution=100.0, save_all=True, append_images=image_objs)
        signals.log_data.emit(f"Done creating pdf : {self.ui.output_file_edit.text()}")

        ## Start the OCR process
        command = f"python -m ocrmypdf"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        while True:
            # Read The incoming Data
            output = process.stdout.readline()
            print(output.decode())

            # Send Read data to GUI logging output
            if output.decode() != '': 
                signals.log_data.emit(f"Worker {process.pid} >> {output.decode()}")

            # Break out of the loop if no more data is comming
            if output.decode() == '' and process.poll() is not None:
                signals.log_data.emit("Done converting ")
                print("Breaking...")
                break
        
        rc = process.poll()
        if rc == 0:
            signals.log_data.emit("Successfully made all the pdf files searchable.")
        else:
            signals.log_data.emit(f"Did not run the command successfully. RETURN CODE: {rc}")

        ## Send finished signal
        signals.finished.emit()

class Worker(QRunnable):

    def __init__(self, func, *args, **kwargs):

        super(Worker, self).__init__()

        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):

        self.func(self.signals)


class WorkerSignals(QObject):
    finished = pyqtSignal()
    log_data = pyqtSignal(object)
    message_signal = pyqtSignal(object)
    ask_question_signal = pyqtSignal(object)







































































if __name__ == "__main__":

    w = QApplication([])
    app = MainApplication()
    app.show()
    w.exec_()





























































































































































































































































































































































































