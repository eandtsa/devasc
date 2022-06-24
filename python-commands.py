# create virtual environment
(base) tandrey@tandrey-a01 devasc % python3 -m venv myvenv
(base) tandrey@tandrey-a01 devasc % source myvenv/bin/activate
(myvenv) (base) tandrey@tandrey-a01 devasc % 
(myvenv) (base) tandrey@tandrey-a01 devasc % 
(myvenv) (base) tandrey@tandrey-a01 devasc % deactivate
(base) tandrey@tandrey-a01 devasc % 

(myvenv) (base) tandrey@tandrey-a01 devasc % pip install urllib3
Collecting urllib3
  Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.0/139.0 kB 937.2 kB/s eta 0:00:00
Installing collected packages: urllib3
Successfully installed urllib3-1.26.9
WARNING: There was an error checking the latest version of pip.
(myvenv) (base) tandrey@tandrey-a01 devasc % 

# Upgrade pip
pip install --upgrade pip

# search packages with pip : https://pypi.org/project/pip-search/
pip install pip_search

(myvenv) (base) tandrey@tandrey-a01 devasc % pip_search -s name ansible      
                                    🐍 https://pypi.org/search/?q=ansible 🐍                                    
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Package               ┃ Version     ┃ Released   ┃ Description                                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 📂 ansible            │ 6.0.0       │ 21-06-2022 │ Radically simple IT automation                            │
│ 📂 ansible-alicloud   │ 1.19.0      │ 22-04-2020 │ Ansible provider for Alicloud.                            │
│ 📂 ansible-api        │ 0.5.1       │ 23-12-2021 │ A restful HTTP API for ansible                            │
│ 📂 ansible-apply      │ 0.1.2       │ 23-02-2019 │ apply remote tasks, supports command line inventory       │
│ 📂 ansible-art        │ 0.3.2       │ 13-07-2016 │ A simple tool to apply role of ansible                    │
│ 📂 ansible-autodoc    │ 0.5.3       │ 02-03-2019 │ Generate documentation from annotated playbooks and roles │
│                       │             │            │ using templates                                           │
│ 📂 ansible-chaos      │ 0.0.1a1     │ 25-09-2020 │                                                           │
│ 📂 ansible-compose    │ 1.0.8.post5 │ 15-02-2019 │ The obscene docker-compose deploy with ansible cli        │
│ 📂 ansible-core       │ 2.13.1      │ 20-06-2022 │ Radically simple IT automation                            │
│ 📂 ansible-doctor     │ 1.4.1       │ 20-06-2022 │ Generate documentation from annotated Ansible roles using │
│                       │             │            │ templates.                                                │
│ 📂 ansible-dotdiff    │ 0.1.5       │ 01-04-2019 │ Nested structure diff library with dot-path notation for  │
│                       │             │            │ Ansible                                                   │
│ 📂 ansible-droplet    │ 0.5.0       │ 13-01-2019 │ A cli to Create / Destroy DigitalOcean Droplets           │
│ 📂 ansible-generator  │ 2.1.4       │ 10-05-2019 │ Generate ansible directory structures                     │
│ 📂 ansible-marathon   │ 0.2.0       │ 12-05-2016 │ An Ansible module for deploying applications to Mesos     │
│                       │             │            │ through Marathon                                          │
│ 📂 ansible-navigator  │ 2.1.0       │ 10-05-2022 │ A text-based user interface (TUI) for the Red Hat Ansible │
│                       │             │            │ Automation Platform                                       │
│ 📂 ansible-nwd        │ 0.8         │ 12-12-2020 │ Ansible role automatic documentation                      │
│ 📂 ansible-parallel   │ 2021.1.22   │ 22-01-2021 │ Run ansible playbooks in parallel.                        │
│ 📂 ansible-please     │ 0.1.20      │ 25-05-2021 │ Helper package to make running Ansible a bit smoother     │
│ 📂 ansible-repo       │ 1.0.4       │ 08-06-2020 │                                                           │
│ 📂 ansible-roster     │ 1.0.1       │ 31-05-2022 │ Host based Ansible yaml inventory                         │
│ 📂 ansible-run        │ 3.6         │ 22-10-2018 │                                                           │
│ 📂 ansible-solace     │ 0.7.8       │ 29-12-2020 │ Ansible modules to configure Solace PubSub+ event brokers │
│                       │             │            │ with SEMP.                                                │
│ 📂 ansible-starter    │ 0.1.1       │ 05-01-2020 │ Bash script for creating fully functional ansible         │
│                       │             │            │ project.                                                  │
│ 📂 ansible-stubs      │ 0.1.dev1    │ 11-05-2020 │ ansible-stubs aids in the development and testing of      │
│                       │             │            │ Ansible roles                                             │
│ 📂 ansible-terminal   │ 0.14.1      │ 03-01-2021 │ SSH/SFTP Terminal Manager for Ansible                     │
│ 📂 ansible-tests      │ 0.0.4       │ 13-11-2018 │                                                           │
│ 📂 ansible-toolbox    │ 0.3         │ 02-11-2017 │ https://github.com/larsks/ansible-toolbox                 │
│ 📂 ansible-toolkit    │ 1.3.2       │ 16-10-2015 │ The missing Ansible tools                                 │
│ 📂 ansible-tools      │ 0.2.0       │ 29-03-2020 │ Keyring integration and local execution wrappers for      │
│                       │             │            │ Ansible                                                   │
│ 📂 ansible-virl       │ 0.0.7       │ 30-04-2020 │ Cisco DevNet VIRL Ansible Modules                         │
│ 📂 groot-ansible      │ 0.4.2       │ 31-12-2020 │ system installation and update scripts                    │
│ 📂 kolla-ansible      │ 14.1.0      │ 07-06-2022 │ Ansible Deployment of Kolla containers                    │
│ 📂 mist.ansible       │ 0.1.8       │ 24-09-2014 │ Ansible modules for the mist.io service                   │
│ 📂 moban-ansible      │ 0.0.2       │ 04-09-2020 │ Ansible filters, tests and utility functions for moban    │
│                       │             │            │ users                                                     │
│ 📂 networking-ansible │ 5.0.0       │ 14-10-2020 │ Ansible Networking ML2 Driver                             │
│ 📂 ploy_ansible       │ 1.4.1       │ 11-02-2018 │ Plugin to integrate Ansible with ploy.                    │
│ 📂 pocker-ansible     │ 0.2.0       │ 23-03-2016 │ Collection of ansible plugins for docker orchestration    │
│                       │             │            │ using pocker library                                      │
│ 📂 pyateos-ansible    │ 1.0.7       │ 02-09-2020 │ Ansible module pyATEOS framework.                         │
│ 📂 pytest-ansible     │ 2.2.4       │ 25-05-2021 │ Plugin for py.test to simplify calling ansible modules    │
│                       │             │            │ from tests or fixtures                                    │
│ 📂 waldur-ansible     │ 0.6.2       │ 05-07-2018 │ Waldur plugin for Ansible playbooks management and        │
│                       │             │            │ execution.                                                │
└───────────────────────┴─────────────┴────────────┴───────────────────────────────────────────────────────────┘
(myvenv) (base) tandrey@tandrey-a01 devasc % 

# install packages from list on file 
touch requeremets.txt (with packages)

pip install -r requeremets.txt
