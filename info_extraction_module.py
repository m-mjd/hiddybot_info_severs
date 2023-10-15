def extract_info_from_json(data):
    system_stats = data.get('stats', {}).get('system', {})
    top5_stats = data.get('stats', {}).get('top5', {})
    usage_history = data.get('usage_history', {})
    bytes_recv = system_stats.get('bytes_recv')
    bytes_recv_cumulative = system_stats.get('bytes_recv_cumulative')
    bytes_sent = system_stats.get('bytes_sent')
    bytes_sent_cumulative = system_stats.get('bytes_sent_cumulative')
    cpu_percent = system_stats.get('cpu_percent')
    number_of_cores = system_stats.get('num_cpus')
    disk_total = system_stats.get('disk_total')
    disk_used = system_stats.get('disk_used')
    ram_total = system_stats.get('ram_total')
    ram_used = system_stats.get('ram_used')
    total_upload_server = system_stats.get('net_sent_cumulative_GB')
    total_download_server = system_stats.get('net_total_cumulative_GB')
    hiddify_used = system_stats.get('hiddify_used')
    load_avg_15min = system_stats.get('load_avg_15min')
    load_avg_1min = system_stats.get('load_avg_1min')
    load_avg_5min = system_stats.get('load_avg_5min')
    total_connections = system_stats.get('total_connections')
    total_unique_ips = system_stats.get('total_unique_ips')
    cpu_top5 = top5_stats.get('cpu', [])
    memory_top5 = top5_stats.get('memory', [])
    ram_top5 = top5_stats.get('ram', [])
    online_last_24h = usage_history.get('h24', {}).get('online')
    usage_last_24h = usage_history.get('h24', {}).get('usage')
    online_last_30_days = usage_history.get('last_30_days', {}).get('online')
    usage_last_30_days = usage_history.get('last_30_days', {}).get('usage')
    online_last_5min = usage_history.get('m5', {}).get('online')
    usage_last_5min = usage_history.get('m5', {}).get('usage')
    online_today = usage_history.get('today', {}).get('online')
    usage_today = usage_history.get('today', {}).get('usage')
    online_total = usage_history.get('total', {}).get('online')
    usage_total = usage_history.get('total', {}).get('usage')
    total_users = usage_history.get('total', {}).get('users')
    online_yesterday = usage_history.get('yesterday', {}).get('online')
    usage_yesterday = usage_history.get('yesterday', {}).get('usage')

    return {
        'bytes_recv': bytes_recv,
        'bytes_recv_cumulative': bytes_recv_cumulative,
        'bytes_sent': bytes_sent,
        'bytes_sent_cumulative': bytes_sent_cumulative,
        'cpu_percent': cpu_percent,
        'number_of_cores': number_of_cores,
        'disk_total': disk_total,
        'disk_used': disk_used,
        'ram_total': ram_total,
        'ram_used': ram_used,
        'total_upload_server': total_upload_server,
        'total_download_server': total_download_server,
        'hiddify_used': hiddify_used,
        'load_avg_15min': load_avg_15min,
        'load_avg_1min': load_avg_1min,
        'load_avg_5min': load_avg_5min,
        'total_connections': total_connections,
        'total_unique_ips': total_unique_ips,
        'cpu_top5': cpu_top5,
        'memory_top5': memory_top5,
        'ram_top5': ram_top5,
        'online_last_24h': online_last_24h,
        'usage_last_24h': usage_last_24h,
        'online_last_30_days': online_last_30_days,
        'usage_last_30_days': usage_last_30_days,
        'online_last_5min': online_last_5min,
        'usage_last_5min': usage_last_5min,
        'online_today': online_today,
        'usage_today': usage_today,
        'online_total': online_total,
        'usage_total': usage_total,
        'total_users': total_users,
        'online_yesterday': online_yesterday,
        'usage_yesterday': usage_yesterday,
    }
