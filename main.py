import os
import sys
from tabulate import tabulate
import random

# Project template
class Project:
    def __init__(self, index, status, client_name, start_date, end_date, task_month, job, price):
        self.index = int(index)
        self.status = status
        self.client_name = client_name
        self.start_date = start_date
        self.end_date = end_date
        self.task_month = task_month
        self.job = job
        self.price = int(price)
    
    def as_list(self):
        return [
            self.index,
            self.status,
            self.client_name,
            self.start_date,
            self.end_date,
            self.task_month,
            self.job,
            self.price
        ]

# Util helper
class Util:
    def __init__(self):
        self.projects = []
        self.FetchDirectory()

    def StatusStructure(self,param):
        return 'Done' if param == 'D' else 'Not Done'

    def FetchDirectory(self):
        # get current directory
        current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
        all_directories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]
        
        # adapt to list of Project
        for directory in all_directories:
            try:
                index, raw_name = directory.split('.')
                raw_name = raw_name[1:]
                raw_split = raw_name.split('-')

                raw_client_name = raw_split[0] 
                raw_client_name = raw_client_name[1:len(raw_client_name)-1]

                status, raw_client_name = raw_client_name.split(']')
                client_name = raw_client_name[1:]

                status = self.StatusStructure(status)

                start_date = raw_split[1] 
                start_date = start_date[1:]

                raw_end_date = raw_split[2]
                end_date, raw_task_month = raw_end_date.split(' ')
                
                task_month = raw_task_month[:len(raw_task_month)-1]

                raw_job = raw_split[3]
                raw_job = raw_job[1:]
                raw_job = raw_job[:len(raw_job)-2]
                
                raw_job, price = raw_job.split('[')
                job = raw_job[:len(raw_job)-1]

                self.projects.append(
                    Project(
                        index,
                        status,
                        client_name,
                        start_date,
                        end_date,
                        task_month,
                        job,
                        price,
                    )
                )

            except Exception as e:
                print(f"Error processing directory '{directory}': {e}")

    def TotalPrice(self):
        total = 0
        for project in self.projects:
            total = total + int(project.price)
        return total
    
    def TotalProject(self):
        return len(self.projects)

    def DisplayAllProject(self):
        # sorted by index
        projects_table_sorted = sorted(self.projects, key=lambda x: x.index, reverse=True)
        projects_table = [project.as_list() for project in projects_table_sorted]
        
        headers = ["Index", "Status", "Client Name", "Start Date", "End Date", "Task Month", "Job", "Price (K)"]
        table = tabulate(projects_table, headers=headers, tablefmt="pretty")
        print(table)

randomText = [
    'Hola fellas, you find me',
    'Bite the bullet',
    'Hit the hay',
    'Break a leg',
    'Jump on the bandwagon',
    'Cost an arm and a leg',
    'Cut to the chase',
    'Burning the midnight oil',
    'The ball is in your court',
    'Piece of cake',
    'The early bird catches the worm',
    'Let the cat out of the bag',
    'Throw in the towel',
    'Under the weather',
    'Burn the midnight oil',
    'A piece of cake',
    'Hit the nail on the head',
    'The whole nine yards'
]

util = Util()
random_index = random.randint(0, len(randomText) - 1)

print(f'\n{randomText[random_index]}!! congratulations you have done {util.TotalProject()} project(s), with total {util.TotalPrice()}K!')
print(util.DisplayAllProject())

input("\npress enter to continue...")
