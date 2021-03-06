# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
import time
#END_HEADER


class stressTest:
    '''
    Module Name:
    stressTest

    Module Description:
    A KBase module: stressTest
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://bio-boris@github.com/bio-boris/stress.git"
    GIT_COMMIT_HASH = "de70bb2f6a585c5e74462a1fb2d301eb27dab948"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.report = KBaseReport(self.callback_url)
        #END_CONSTRUCTOR
        pass


    def run_stressTest(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_stressTest
        cpu = params['cpu']
        memory = params['memory_mb']
        command = f"stress -c {cpu} -i 1 -m 1 --vm-bytes {memory}M -t 360s"
        time.sleep(1200)

        report_info = self.report.create({'report': {'objects_created':[],
                                                'text_message': cpu + ":" +  memory + ":" + command},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_stressTest

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_stressTest return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def run_stressTest2(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_stressTest2
        cpu = params['cpu']
        memory = params['memory_mb']
        command = f"stress -c {cpu} -i 1 -m 1 --vm-bytes {memory}M -t 360s"
        time.sleep(1200)

        report_info = self.report.create({'report': {'objects_created':[],
                                                'text_message': cpu + ":" +  memory + ":" + command},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_stressTest2

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_stressTest2 return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def run_stressTest3(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_stressTest3
        cpu = params['cpu']
        memory = params['memory_mb']
        command = f"stress -c {cpu} -i 1 -m 1 --vm-bytes {memory}M -t 360s"
        time.sleep(1200)

        report_info = self.report.create({'report': {'objects_created':[],
                                                'text_message': cpu + ":" +  memory + ":" + command},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_stressTest3

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_stressTest3 return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
