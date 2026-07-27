from flask import Flask, request, render_template
import math
import ipaddress #subnet icin
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

'''
APP1-Network_Subnet_Planner
Host sayısı
      ↓
CIDR hesapla
      ↓
Subnet mask hesapla
      ↓
Class seç
      ↓
Base network belirle
      ↓
ipaddress ile
Network Address
Broadcast
Host Range
hesapla
'''

@app.route("/Network_Subnet_Planner", methods=["GET", "POST"])
def app1():
    if request.method == "GET":
        return render_template("NetworkSubnetPlanner.html")
    if request.method == "POST":
        #girdiyi alma
        host_num = int(request.form["host_num"])  #html de int yazsak dahi flask her zaman str getiri html den bu yuzden int donusumu yapiyoruz

        #network id ve broadcast icn iki adres ekle
        needed_addresses = host_num+2

        #kac bit kullandigimi buldum power kac cikarsa o kadar bit kullandimm
        ''' 
        bu yontem de kullanilabilir
        power = 0
        address = 1
        while address < needed_addresses:
              power=power+1
              address=address*2
        '''

        power = math.ceil(math.log2(needed_addresses))
        #math.log2 gerekli host adreslerini karsilayacak en kucuk 2 nin kuvvetini bulur
        #math.ceil sonucu yukari yuvarlayarak yeterli subnet kapasitesini garanti eder
        network_bits = 32-power #CIDR prefix /28 /24 gibi falan

        #255.255.255.240 gibi ornegin
        mask_network = ipaddress.IPv4Network(f"0.0.0.0/{network_bits}") #mesela 4 bit kullandik kaldi 28 /28 olucak bana subnet mask vericek
        subnet_mask=str(mask_network.netmask) #subnet bulmak icin yani agdan kac addresslik yer acilmali onu ogrenmek icin

        #class lari ayiriyorum
        if needed_addresses <= 254:
            network_class = 'Class C'
            base_network = "192.168.0.0"
        elif needed_addresses <= 65534:
            network_class = 'Class B'
            base_network = "172.16.0.0"
        else:
            network_class = 'Class A'
            base_network = "10.0.0.0"

        #assign edilen ag
        assigned_network= ipaddress.IPv4Network(f"{base_network}/{network_bits}")

        ''' python iki defa liste olusturuyor gereksiz islem
        first_element=list(assigned_network.hosts())[0] #ilk host
        last_element=list(assigned_network.hosts())[-1] #son host
        '''
        host_list = list(assigned_network.hosts()) #bir kez liste olustrursun
        first_element = host_list[0]
        last_element = host_list[-1]

        total_host_capacity = len(host_list) #listedeki eleman sayisi

        #terminal ciktisi
        print("[ASSIGNMENT RESOLUTION REPORT]")
        print(f"Target Host Requirements: {host_num} ")
        print(f"Allocated Network Boundary: {network_class}")
        print(f"Optimized Prefix Length: /{network_bits}")
        print(f"Generated Subnet Mask: {subnet_mask}")
        print(f"Assigned Network Address: {assigned_network.network_address}")
        print(f"Usable Host Address Range: {first_element} -> {last_element}")
        print(f"Calculated Broadcast IP: {assigned_network.broadcast_address}")
        print(f"Total Subnet Host Capacity: {total_host_capacity} usable slots")


        #print(assigned_network.network_address) terminalde bu kodlarin cevaplari oluyor ama biz html ile gostericez
        return render_template(
            "NetworkSubnetPlanner.html",
            host_num=host_num,
            network_class=network_class,
            network_bits=network_bits,
            subnet_mask=subnet_mask,
            network_address=assigned_network.network_address,
            first_element=first_element,
            last_element=last_element,
            broadcast_address=assigned_network.broadcast_address,
            total_host_capacity=total_host_capacity
        )

@app.route("/app2")
def app2():
    return render_template("app2.html")

@app.route("/app3")
def app3():
    return render_template("app3.html")

if __name__ == "__main__":
    app.run(debug=True)