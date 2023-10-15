import sqlite3
from urllib.parse import urlparse
from info_extraction_module import extract_info_from_json
import requests

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


def scrape_data_from_json_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse JSON data
        json_data = response.json()

        # Extract information from JSON using the shared function
        extracted_data = extract_info_from_json(json_data)

        return extracted_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None



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
            link = (f"{link}/admin/get_data/")
            result = scrape_data_from_json_url(link)

            bytes_recv = result.get('bytes_recv', 'N/A')
            bytes_recv_cumulative = result.get('bytes_recv_cumulative', 'N/A')
            bytes_sent = result.get('bytes_sent', 'N/A')
            bytes_sent_cumulative = result.get('bytes_sent_cumulative', 'N/A')
            cpu_percent = result.get('cpu_percent', 'N/A')
            number_of_cores = result.get('number_of_cores', 'N/A')
            disk_total = result.get('disk_total', 'N/A')
            disk_used = result.get('disk_used', 'N/A')
            ram_total = result.get('ram_total', 'N/A')
            ram_used = result.get('ram_used', 'N/A')
            total_upload_server = result.get('total_upload_server', 'N/A')
            total_download_server = result.get('total_download_server', 'N/A')
            online_last_24h = result.get('online_last_24h', 'N/A')
            usage_last_24h = result.get('usage_last_24h', 'N/A')
            online_last_30_days = result.get('online_last_30_days', 'N/A')
            usage_last_30_days = result.get('usage_last_30_days', 'N/A')
            online_last_5min = result.get('online_last_5min', 'N/A')
            usage_last_5min = result.get('usage_last_5min', 'N/A')
            online_today = result.get('online_today', 'N/A')
            usage_today = result.get('usage_today', 'N/A')
            online_total = result.get('online_total', 'N/A')
            usage_total = result.get('usage_total', 'N/A')
            total_users = result.get('total_users', 'N/A')
            online_yesterday = result.get('online_yesterday', 'N/A')
            usage_yesterday = result.get('usage_yesterday', 'N/A')
            hiddify_used = result.get('hiddify_used', 'N/A')
            load_avg_15min = result.get('load_avg_15min', 'N/A')
            load_avg_1min = result.get('load_avg_1min', 'N/A')
            load_avg_5min = result.get('load_avg_5min', 'N/A')
            total_connections = result.get('total_connections', 'N/A')
            total_unique_ips = result.get('total_unique_ips', 'N/A')
            cpu_top5 = result.get('cpu_top5', 'N/A')
            memory_top5 = result.get('memory_top5', 'N/A')
            ram_top5 = result.get('ram_top5', 'N/A')

            # Calculate percentage for RAM and Disk
            ram_percent = (ram_used / ram_total) * \
                100 if ram_total != 'N/A' and ram_total != 0 else 'N/A'
            disk_percent = (disk_used / disk_total) * \
                100 if disk_total != 'N/A' and disk_total != 0 else 'N/A'

            # Format bytes with appropriate units
            formatted_bytes_recv = f"{bytes_recv / (1024 ** 2):.2f} MB" if bytes_recv != 'N/A' else 'N/A'
            formatted_bytes_sent = f"{bytes_sent / (1024 ** 2):.2f} MB" if bytes_sent != 'N/A' else 'N/A'

            # Add information for all servers
            all_server_info += f"\n{lline}\nServer : {server_name}\n{lline}\n*** USAGE SERVER ***\n\n" \
                               f"!!! SYS INFO !!!\n\n"\
                               f"CPU: {cpu_percent}% - {number_of_cores} CORE\n" \
                               f"RAM: {ram_used:.2f} / {ram_total:.2f} ({ram_percent:.2f}%)\n" \
                               f"DISK: {disk_used:.2f} / {disk_total:.2f} ({disk_percent:.2f}%)\n\n" \
                               f"!!! NETWORK INFO !!!\n\n"\
                               f"Now Bytes Received: {formatted_bytes_recv}\n" \
                               f"Now Bytes Sent: {formatted_bytes_sent}\n" \
                               f"Total Upload (Server): {total_upload_server}\n" \
                               f"Total Download (Server): {total_download_server}\n" \
                               f"Total Users: {total_users}\n" \
                               f"Online (Last 5 min): {online_last_5min}\n" \
                               f"Online (Today): {online_today}\n" \
                               f"Usage (Today): {usage_today}\n" \
                               f"Online(30 Days): {online_last_30_days}\n" \
                               f"Usage(30 Days): {usage_last_30_days}\n"\



get_server_status()




