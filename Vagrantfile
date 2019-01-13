# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Box que vamos a utilizar en la máquina virtual.
  config.vm.box = "noticieroapp"
  # Especificamos el dummy box, el cual nos proporcionará una base para nuestra máquina.
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'

  # Le especificamos la clave, para la conexión mediante ssh de la máquina.
	config.ssh.private_key_path = "~/.ssh/id_rsa"
  
  	# Configuración de la máquina (proveedor) donde vamos a crear el host de la máquina:
	config.vm.provider :azure do |noticiero, override|

		# Variables de entorno y parámetros, necesarios para crear nuestra máquina con Azure.
	    	noticiero.tenant_id = ENV['AZURE_TENANT_ID']  # Tenant id
	    	noticiero.client_id = ENV['AZURE_CLIENT_ID'] #Id del cliente de azure
	    	noticiero.client_secret = ENV['AZURE_CLIENT_SECRET']  #Contraseña de del cliente de azure
	    	noticiero.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']  #Subscripción de Azure.

		# Tamaño de los recursos de Azure
		noticiero.vm_size = "Standard_A0"
		# Localización donde queremos el host, o la granja de servidores donde
		# nos asignan la máquina
		noticiero.location = "westeurope"
		#Abrimos el puerto 80, que es el que vamos a utilizar
		noticiero.tcp_endpoints = "80"
		#Nombre de la máquina virtual
		noticiero.vm_name = "noticiero"
		#Especificamos la imagen que vamos a montar en nuestra máquina, en este caso Ubuntu 16.04
		noticiero.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
		#Grupo de recursos en los que se creará la máquina.
		noticiero.resource_group_name = 'ProyectoNoticieroApp'
	  end

  # Configuración del provisionamiento con ansible, con nuestro fichero de playbook.yml
  # Durante el vagrant up, nos permite que el fichero playbook.yml nos instale las dependencias que necesita
  # nuestra máquina
	config.vm.provision :ansible do |ansible|
		ansible.playbook = "./provision/playbook.yml"
	end
end
