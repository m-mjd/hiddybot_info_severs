import sqlite3
from urllib.parse import urlparse
import site_info_modele
import re

sim = site_info_modele
rewidth = r'width: '
lline = (32 * "-")

all_server_info = ""


def extract_links(text):
    links = []
    words = text.split()
    for word in words:
        parsed_url = urlparse(word)
        if parsed_url.scheme and parsed_url.netloc:
            links.append(word)
    return links


def get_server_status():
    global all_server_info

    db_connection = sqlite3.connect('Database/hidybot.db')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM servers')
    rows = cursor.fetchall()
    cursor.close()
    db_connection.close()

    for row in rows:
        server_name = row[2]
        result1 = extract_links(row[1])
        for link in result1:
            link = (f"{link}/admin")
            result = sim.scrape_data_from_url(link)

            today_info_title, today_info_number, today_info_progress, today_info_description = result[
                'today']
            yesterday_info_title, yesterday_info_number, yesterday_info_progress, yesterday_info_description = result[
                'yesterday']
            monthly_info_title, monthly_info_number, monthly_info_progress, monthly_info_description = result[
                'monthly']
            total_info_title, total_info_number, total_info_progress, total_info_description = result[
                'total']
            network_info_title, network_info_number, network_info_progress, network_info_description = result[
                'network']
            cpu_info_title, cpu_info_number, cpu_info_progress, cpu_info_description = result[
                'cpu']
            ram_info_title, ram_info_number, ram_info_progress, ram_info_description = result[
                'ram']
            disk_title, disk_usage, disk_progress, disk_description = result['disk']
            online_users_title, online_users_number, online_users_progress, online_users_description = result[
                'online_users']

            cpu_info_progress = re.sub(rewidth, "", cpu_info_progress)
            cpu_info_progress = float(cpu_info_progress.rstrip('%'))
            ram_info_progress = re.sub(rewidth, "", ram_info_progress)
            ram_info_progress = float(ram_info_progress.rstrip('%'))
            ram_info_progress += 10
            disk_progress = re.sub(rewidth, "", disk_progress)
            disk_progress = float(disk_progress.rstrip('%'))
            online_users_progress = re.sub(rewidth, "", online_users_progress)
            online_users_progress = float(online_users_progress.rstrip('%'))
            today_info_progress = re.sub(rewidth, "", today_info_progress)
            today_info_progress = float(today_info_progress.rstrip('%'))
            yesterday_info_progress = re.sub(
                rewidth, "", yesterday_info_progress)
            yesterday_info_progress = float(
                yesterday_info_progress.rstrip('%'))
            monthly_info_progress = re.sub(rewidth, "", monthly_info_progress)
            monthly_info_progress = float(monthly_info_progress.rstrip('%'))
            total_info_progress = re.sub(rewidth, "", total_info_progress)
            total_info_progress = float(total_info_progress.rstrip('%'))
            cpu_info_progress = round(cpu_info_progress, 2)
            ram_info_progress = round(ram_info_progress, 2)
            disk_progress = round(disk_progress, 2)
            online_users_progress = round(online_users_progress, 2)
            today_info_progress = round(today_info_progress, 2)
            yesterday_info_progress = round(yesterday_info_progress, 2)
            monthly_info_progress = round(monthly_info_progress, 2)
            total_info_progress = round(total_info_progress, 2)
            cpu_info_progress = f"{cpu_info_progress}%"
            ram_info_progress = f"{ram_info_progress}%"
            disk_progress = f"{disk_progress}%"
            online_users_progress = f"{online_users_progress}%"
            today_info_progress = f"{today_info_progress}%"
            yesterday_info_progress = f"{yesterday_info_progress}%"
            monthly_info_progress = f"{monthly_info_progress}%"
            total_info_progress = f"{total_info_progress}%"

            all_server_info += f"\n{lline}\nServer : {server_name}\n{lline}\n*** USAGE SERVER ***\n\nCPU: {cpu_info_progress}\nRAM: {ram_info_progress}\nDISK: {disk_progress}\n\n*** USAGE ACOUNTS ***\n\nNow\nusage_data : {online_users_number}\nConnected accounts : {online_users_progress} \n\nToday:\nusage_data : {today_info_number}\nConnected accounts : {today_info_progress} \n\nYesterday\nusage_data : {yesterday_info_number}\nConnected accounts : {yesterday_info_progress} \n\nMonth:\nusage_data : {monthly_info_number}\nConnected accounts : {monthly_info_progress} \n\nTotal:\nusage_data : {total_info_number}\nConnected accounts : {total_info_progress} \n"


get_server_status()
