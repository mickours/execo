# Copyright 2009-2012 INRIA Rhone-Alpes, Service Experimentation et
# Developpement
#
# This file is part of Execo.
#
# Execo is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Execo is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Execo.  If not, see <http://www.gnu.org/licenses/>

from execo.config import load_configuration, get_user_config_filename

# _STARTOF_ g5k_configuration
g5k_configuration = {
    'kadeploy3': 'kadeploy3',
    'kadeploy3_options': '-k -d',
    'default_env_name': None,
    'default_env_file': None,
    'default_timeout': 900,
    'check_deployed_command': "! (mount | grep -E '^/dev/[[:alpha:]]+2 on / ')",
    'no_ssh_for_local_frontend' : False,
    'polling_interval' : 60,
    'tiny_polling_interval' : 10,
    }
# _ENDOF_ g5k_configuration
"""Global Grid5000 configuration parameters.

- ``kadeploy3``: kadeploy3 command.

- ``kadeploy3_options``: common kadeploy3 command line options.

- ``default_env_name``: a default environment name to use for
  deployments (as registered to kadeploy3).

- ``default_env_file``: a default environment file to use for
  deployments (for kadeploy3).

- ``default_timeout``: default timeout for all calls to g5k services
  (except deployments).

- ``check_deployed_command``: default shell command used by `deploy`
  to check that the nodes are correctly deployed. This command should
  return 0 if the node is correctly deployed, or another value
  otherwise. The default checks that the root is not on the second
  partition of the disk.

- ``no_ssh_for_local_frontend``: if True, don't use ssh to issue g5k
  commands for local site. If False, always use ssh, both for remote
  frontends and local site. Set it to True if you are sure that your
  scripts always run on the local frontend.

- ``polling_interval``: time interval between pollings for various
  operations, eg. wait oar job start.

- ``tiny_polling_interval``: small time interval between pollings for
  various operations, used for example when waiting for a job start,
  and start date of the job is over but the job is not yet in running
  state.
"""

# _STARTOF_ default_oarsh_oarcp_params
default_oarsh_oarcp_params = {
    'user':        None,
    'keyfile':     None,
    'port':        None,
    'ssh':         'oarsh',
    'scp':         'oarcp',
    'taktuk':      'taktuk',
    'ssh_options': ( '-tt',
                     '-o', 'BatchMode=yes',
                     '-o', 'PasswordAuthentication=no',
                     '-o', 'StrictHostKeyChecking=no',
                     '-o', 'UserKnownHostsFile=/dev/null',
                     '-o', 'ConnectTimeout=20' ),
    'scp_options': ( '-o', 'BatchMode=yes',
                     '-o', 'PasswordAuthentication=no',
                     '-o', 'StrictHostKeyChecking=no',
                     '-o', 'UserKnownHostsFile=/dev/null',
                     '-o', 'ConnectTimeout=20',
                     '-rp' ),
    'taktuk_options': ( '-s', ),
    'taktuk_connector': 'oarsh',
    'taktuk_connector_options': ( '-o', 'BatchMode=yes',
                                  '-o', 'PasswordAuthentication=no',
                                  '-o', 'StrictHostKeyChecking=no',
                                  '-o', 'UserKnownHostsFile=/dev/null',
                                  '-o', 'ConnectTimeout=20'),
    'ssh_scp_pty': True,
    'host_rewrite_func': lambda host: host
    }
# _ENDOF_ default_oarsh_oarcp_params
"""A convenient, predefined connexion paramaters dict with oarsh / oarcp configuration.

See `execo.default_connexion_params`
"""

# _STARTOF_ default_frontend_connexion_params
default_frontend_connexion_params = {
    'user':        None,
    'keyfile':     None,
    'port':        None,
    'ssh':         'ssh',
    'scp':         'scp',
    'taktuk':      'taktuk',
    'ssh_options': ( '-tt',
                     '-o', 'BatchMode=yes',
                     '-o', 'PasswordAuthentication=no',
                     '-o', 'StrictHostKeyChecking=no',
                     '-o', 'UserKnownHostsFile=/dev/null',
                     '-o', 'ConnectTimeout=20' ),
    'scp_options': ( '-o', 'BatchMode=yes',
                     '-o', 'PasswordAuthentication=no',
                     '-o', 'StrictHostKeyChecking=no',
                     '-o', 'UserKnownHostsFile=/dev/null',
                     '-o', 'ConnectTimeout=20',
                     '-rp' ),
    'taktuk_options': ( '-s', ),
    'taktuk_connector': 'ssh',
    'taktuk_connector_options': ( '-o', 'BatchMode=yes',
                                  '-o', 'PasswordAuthentication=no',
                                  '-o', 'StrictHostKeyChecking=no',
                                  '-o', 'UserKnownHostsFile=/dev/null',
                                  '-o', 'ConnectTimeout=20'),
    'ssh_scp_pty': False,
    'host_rewrite_func': lambda host: host + ".grid5000.fr"
    }
# _ENDOF_ default_frontend_connexion_params
"""Default connexion params when connecting to a Grid5000 frontend."""

load_configuration(
  get_user_config_filename(),
  ((g5k_configuration, 'g5k_configuration'),
   (default_frontend_connexion_params, 'default_frontend_connexion_params'),
   (default_oarsh_oarcp_params, 'default_oarsh_oarcp_params')))