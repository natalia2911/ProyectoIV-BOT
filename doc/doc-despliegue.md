# Despliegue en Azure

Para hacer el despliegue en Azure lo primero que tenemos que hacer es crearnos una cuenta en Azure, y usar los créditos que el profesor de la asignatura nos ha proporcionado para usar.

Instalamos el cliente de Azure:

`	curl -L https://aka.ms/InstallAzureCli | bash
`

Nos logeamos :  `az login`

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/login.png)

Procedemos a obtener una serie de datos que necesitamos para crear lo que será nuestro [Vagrantfile](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/Vagrantfile)

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

Una vez realizado esto, deberemos instalar el plugin de azure para vagrant.

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

En el caso en que nuuestro **playbook.yml** no se haya ejecutado a la hora de crear la máquina, lo podremos hacer desde terminal con esta orden:

`ansible-playbook provision/playbook.yml
`

 Para hacer el despliegue tendremos que crear el archivo `fabfile.py` que realizará una serie de ordenes de forma remota mediante ssh.
 Las tareas que puede realizar es conectarse al servidor remoto, actualizar el repositorio, borrar los datos del código antiguo..

Las funciones que hemos definido son:

 - Desinstalar: borra todo el repositorio, el código anterior
 - Instalar: se instala la aplicación
 - Iniciar: lanza la aplicación y la ejecuta en segundo plano.
 -
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/desinstalar.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/instalar.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/iniciar.png)

Para poder probar las funciones del despliegue:

`fab -f despliegue/fabfile.py -H vagrant@noticieroapp.westeurope.cloudapp.azure.com <Iniciar/Instalar/Desinstalar>`

Por último, el despliegue final lo hemos realizado:

`IP : 13.80.251.123`

`DNS : noticieroapp.westeurope.cloudapp.azure.com`

Podemos comprobar que ahora la maquina virtual está efectivamente ejecutando el servicio:

![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/ip.png)
![](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/img/dns.png)

Aquí me gustaría hacer un apunte sobre nuestro fichero **fabfile**, en el podríamos haber puesto la ejecución de los test de la siguiente manera:

    def test():
        with cd("ProyectoIV-BOT/test/"):
            result = run("python3 test.py")
        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("Aborting at user request.")

Pero hemos decidido que esta parte la dejaremos para próximas mejoras, esto lo hemos conocido consultado la documentación concretamente de la página : http://docs.fabfile.org/en/1.14/tutorial.html

Aquí adjuntamos los enlaces a la documentación que hemos usado para crear y desplegar nuestra aplicación:

**Fabfile**
https://moduslaborandi.net/post/introduccion-a-fabric-ii/
https://axiacore.com/blog/sudo-y-fabric-para-administrar-y-desplegar-como-devop/
https://blocknitive.com/blog/workshop-hyperledger-fabric-despliegue-de-una-red-fabric-para-universidades/
https://docs.fabfile.org/en/1.4.3/
http://docs.fabfile.org/en/1.14/tutorial.html

**Vagrantfile**
https://www.rubydoc.info/gems/vagrant-azure/1.3.0

**Ansible : Playbook**
https://blog.deiser.com/es/primeros-pasos-con-ansible
https://stackoverrun.com/es/q/7574013
