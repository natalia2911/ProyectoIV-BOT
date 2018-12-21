# Despliegue en Azure

Para hacer el despliege en Azure lo primero que tenemos que hacer es crearnos una cuenta en Azure, y usar los creditos que el profesor de la asignatura nos ha proporcionado para usarlos.

Después tendremos que instalar una serie de paquetes básicos como son:

`
sudo apt-get update && sudo apt-get install -y python libssl-dev libffi-dev python-dev build-essential
`

Instalamos el cliente de Azure:

`	curl -L https://aka.ms/InstallAzureCli | bash
`


Nos logeamos :  `az login`

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/login.png)

Procedemos a obtener una serie de datos que necesitamos para crear lo que será nuestro **Vagrantfile**

Necesitamos obtener:

   - ID del cliente
   - ID secreto del cliente
   - Tenant ID
   - Suscripción

Para obtener los tres primeros datos ejecutaremos
```
az ad sp create-for-rbac
```
Por terminal nos aparecerá algo así:

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/datos.png)


Para obtener la suscripción :
```
az account list --query "[?isDefault].id" -o tsv
```

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/subscripcion.png)

Estos 4 datos los necesitaremos exportar como variables de entorno para el archivo Vagrantfile.

Una vez realizado esto, deberemos instalar el plugin de azure para vagrant:
```
 - vagrant plugin install vagrant-azure
 - npm install azure-cli -g
```

Procedemos a añadir el box a vagrant:
```
vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
```

Creamos el archivo **Vagrantfile** :
```
vagrant init azure
```
Crearemos el archivo de aprovisionamiento para la máquina, donde tendremos todo lo que esta necesitará, en nuestro caso se llamará `playbook.yml`

Y ya podemos iniciar la máquina virtual:
```
vagrant up --provider=azure
```

En este pasó se ejecutará el fichero de aprovisionamiento, pero antes deberemos añadir nuestro host  en el fichero : `/etc/ansible/hosts`
podremos poner, tanto nuestra IP de la máquina (la cual miramos en Azure Portal) o nuestra dirección en nuestro caso: `noticieroapp.westeurope.cloudapp.azure.com `

 Para hacer el despliege tendremos que crear el archivo `fabfile.py` que realizará una serie de ordenes

Las funciones que hemos definido son:

 - Desinstalar:
 - Instalar
 - Iniciar


Para poder probar las funciones del despliegue:

`fab -f despliegue/fabfile.py -H vagrant@noticieroapp.westeurope.cloudapp.azure.com <Iniciar/Instalar/Desinstalar>`

Por último, el despliegue final lo hemos realizado:

IP : 13.80.251.123
DNS : noticieroapp.westeurope.cloudapp.azure.com


Podemos comprobar que ahora la maquina virtual está efectivamente ejecutando el servicio:

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/ip.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/dns.png)
