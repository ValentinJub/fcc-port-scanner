import nmap3

scanner = nmap3.Nmap()

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    result = scanner.nmap_list_scan(target, f"{port_range[0]}-{port_range[1]}")
    ip = next(iter(result))
    if ip == "runtime":
        # check if the target is an IP address or a hostname
        if len(target.split(".")) == 4:
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    hostname = result[ip]["hostname"][0]["name"] if result[ip]["hostname"] else None
    for port in result[ip]["ports"]:
        if port["state"] == "open":
            if int(port["portid"]) not in range(port_range[0], port_range[1] + 1):
                continue
            if verbose: 
                open_ports.append((int(port["portid"]), port["service"]["name"]))
            else:
                open_ports.append(int(port["portid"]))
    
    if verbose:
        if hostname:
            verbose_output = f"Open ports for {hostname} ({ip})\nPORT     SERVICE\n"
        else: verbose_output = f"Open ports for {ip}\nPORT     SERVICE\n"
        for port, name in open_ports:
            space = " " * (9 - len(str(port)))
            verbose_output += f"{port}{space}{name}\n"
        verbose_output = verbose_output[:-1]

    return verbose_output if verbose else open_ports

def greet() -> str:
    print("""
______          _                                                       
| ___ \        | |                                                      
| |_/ /__  _ __| |_     ___  ___ __ _ _ __  _ __   ___ _ __ _ __  _   _ 
|  __/ _ \| '__| __|   / __|/ __/ _` | '_ \| '_ \ / _ \ '__| '_ \| | | |
| | | (_) | |  | |_    \__ \ (_| (_| | | | | | | |  __/ |_ | |_) | |_| |
\_|  \___/|_|   \__|   |___/\___\__,_|_| |_|_| |_|\___|_(_)| .__/ \__, |
                                                           | |     __/ |
                                                           |_|    |___/ 
 _              _   _       _            _   _                          
| |            | | | |     | |          | | (_)                         
| |__  _   _   | | | | __ _| | ___ _ __ | |_ _ _ __                     
| '_ \| | | |  | | | |/ _` | |/ _ \ '_ \| __| | '_ \                    
| |_) | |_| |  \ \_/ / (_| | |  __/ | | | |_| | | | |                   
|_.__/ \__, |   \___/ \__,_|_|\___|_| |_|\__|_|_| |_|                   
        __/ |                                                           
       |___/                                                            
                                                                        
                                                                        
 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______  
|______|______|______|______|______|______|______|______|______|______| 
                                                                        
                                                                       """)