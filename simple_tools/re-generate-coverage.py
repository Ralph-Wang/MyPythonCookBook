#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import codecs
import os.path

ROOT='./'

EXCLUDE_CLASSES = {
        "com.santaba.server.pojo.db": set([
            "EventAlertingDao",
            "AlertingDao",
            "NetflowAggregateCtrlRedis"
            ]),

        "com.santaba.server.critialoperation": set([
            "UpdateAwsAccountCriticalOperation",
            "UpdateAzureAccountCriticalOperation",
            "ImportDataSourcesFromCoreCriticalOperation",
            ]),

        "com.santaba.server.servlet.rest.services.device": set([
            "AWSAccountService",
            "AzureAccountService"
            ]),

        "com.santaba.server.cache": set([
            "NetflowCache.NetFlowQueryResult",
            ]),

        "com.santaba.server.util": set([
            "AgentUtils",
            "WebAppConf"
            ]),

        "com.santaba.server.servlet.api": set([
            "DownloadPublicSDKFile",
            "DownloadUpgradeServlet",
            "ReportUpgradeServlet"
            ]),

        "com.santaba.server.servlet.rest.utils": set([
            "ImportItemsFromCoreUtil"
            ]),

        "com.santaba.server.servlet.rest.services.function": set([
            "AwsFunctions",
            "AzureFunctions"
            ]),

        "com.santaba.server.cron": set([
            "EmailCheckTask",
            "TwilioMonitor.TwilioInitTask",
            ]),

        "com.santaba.server.servlet.graph.plothelper": set([
            "CustomerGraphHelper3",
            "OGraphPlotHelper3",
            "StatsDGraphPlotHelper",
            ])
        }

EXCLUDE_PACKAGES = set([
    "com.santaba.server.deploy.upgrade.dbmigrate",
    "com.santaba.server.servlet.rpc",
    "com.santaba.server.jmx",
    "com.santaba.server.servlet.myadmin.portal",
    "com.santaba.server.servlet.rest.pojos.report",
    "com.santaba.server.servlet.rest.services.setting.collector",
    "com.santaba.server.datamining",
    "com.santaba.server.integration",
    "com.santaba.server.servlet.rpc.debugcmd",
    "com.santaba.server.saml",
    "com.santaba.server.servlet.rest.pojos.setting.integration",
    "com.santaba.server.servlet.portal",
    "com.santaba.server.pojo.domain.integrationv2",
    "com.santaba.server.pojo.domain.aws",
    "com.santaba.server.servlet.rest.services.dashboard.autovisual",
    "com.santaba.server.servlet.rest.services.setting.registry",
    "com.santaba.server.servlet.alerter.pop3",
    "com.santaba.server.servlet.rest.services.report",
    "com.santaba.server.servlet.rest.services.setting.integration",
    "com.logicmonitor.common.lmes",
    "com.santaba.server.servlet.rest.pojos.setting.registry",
    "com.santaba.server.netflow",
    "com.santaba.server.pojo.domain.azure",
    "com.santaba.server.util.twofa",
    "com.santaba.server.util.cloud",
    "com.santaba.server.pojo.domain.integrationv2.task",
    "com.santaba.server.servlet.rest.services.netflo",
    "com.santaba.server.netflow",
    "com.santaba.server.util.wordtemplate",
    "com.santaba.server.servlet.rest.services.miscs",
    "com.santaba.server.servlet.rest.services.setting.dns",
    "com.santaba.server.util.registry",
    "com.santaba.server.netflow.mining",
    "com.santaba.server.integration",
    "com.santaba.server.netflow",
    "com.santaba.server.pojo.domain.azure",
    "com.santaba.server.util.twofa",
    "com.santaba.server.util.cloud",
    "com.santaba.server.reporting",
    "com.santaba.server.servlet.rest.services.netflow",
    "com.santaba.server.servlet.rest.services.setting.zuora",
    "com.santaba.server.servlet.rest.services.debug",
    "com.santaba.server.util.registry",
    "com.santaba.server.servlet.rest.services.setting.support",
    "com.santaba.server.servlet.rest.services.report.autovisual",
    "com.santaba.server.pojo.domain.registry",
    "com.santaba.server.service.netflow",
    "com.santaba.server.servlet.rest.services.setting.skilljar"
    ])

def flatten(lst, ret=None):
    ret = [] if ret is None else ret
    for item in lst:
        if isinstance(item, list):
            flatten(item, ret)
        else:
            ret.append(item)
    return ret

class Metric(object):
    def __init__(self, name, missed=0, total=0):
        self._name = name
        self._missed = missed
        self._total = total

    @property
    def name(self):
        return self._name

    @property
    def missed(self):
        return self._missed

    @missed.setter
    def missed(self, val):
        self._missed = int(val)

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, val):
        self._total = int(val)

    def reset(self):
        self._missed = 0
        self._total = 0

    def coverage(self):
        if self._total == 0:
            return 'n/a'
        return int(100 * self._missed / self._total)

    def __str__(self):
        return str(self.__dict__)
    __repr__ = __str__


class Element(object):
    def __init__(self, fullpath, line=None):
        self._fullpath = fullpath
        self._line = line
        self._instructions = Metric('instructions')
        self._branches = Metric('branches')
        self._cxty = Metric('cxty')
        self._lines = Metric('lines')
        self._methods = Metric('methods')
        self._classes = Metric('classes')

        self._childs = set([])

        self._load()


    def is_root(self):
        return self._line == None

    @property
    def childs(self):
        return self._childs

    def decompose(self):
        self._line.decompose()

    @property
    def name(self):
        return self._name

    @property
    def fullpath(self):
        return self._fullpath

    @property
    def instructions(self):
        return self._instructions

    @property
    def branches(self):
        return self._branches

    @property
    def cxty(self):
        return self._cxty

    @property
    def lines(self):
        return self._lines

    @property
    def methods(self):
        return self._methods

    @property
    def classes(self):
        return self._classes

    def __str__(self):
        return str(self.__dict__)

    def flush_to_disk(self):
        with codecs.open(self._fullpath, mode='wb', encoding='utf-8') as output_file:
            output_file.seek(0)
            output_file.truncate()
            output_file.write(str(self._soup))
            output_file.flush()

    def reset_all_metrics(self):
        self.instructions.reset()
        self.branches.reset()
        self.cxty.reset()
        self.lines.reset()
        self.methods.reset()
        self.classes.reset()

    def rebuild_metrics(self):
        if self.is_page_for_class():
            return
        self.reset_all_metrics()
        for child in self.childs:
            self.instructions.missed += child.instructions.missed
            self.instructions.total += child.instructions.total
            self.branches.missed += child.branches.missed
            self.branches.total += child.branches.total
            self.cxty.missed += child.cxty.missed
            self.cxty.total += child.cxty.total
            self.lines.missed += child.lines.missed
            self.lines.total += child.lines.total
            self.methods.missed += child.methods.missed
            self.methods.total += child.methods.total
            self.classes.missed += child.classes.missed
            self.classes.total += child.classes.total
        if self._line is not None:
            cells = self._line.find_all('td')
            cells[2].string = '%s%%' % (self.instructions.coverage())
            cells[4].string = '%s%%' % (self.branches.coverage())
            cells[5].string = str(self.cxty.missed)
            cells[6].string = str(self.cxty.total)
            cells[7].string = str(self.lines.missed)
            cells[8].string = str(self.lines.total)
            cells[9].string = str(self.methods.missed)
            cells[10].string = str(self.methods.total)
            if not self.is_page_for_class():
                cells[11].string = str(self.classes.missed)
                cells[12].string = str(self.classes.total)
        foots = self._soup.tfoot.find_all('td')
        foots[1].string = '%s of %s' % (self.instructions.missed, self.instructions.total)
        foots[2].string = '%s%%' % (self.instructions.coverage())
        foots[3].string = '%s of %s' % (self.branches.missed, self.branches.total)
        foots[4].string = '%s%%' % (self.instructions.coverage())
        foots[5].string = str(self.cxty.missed)
        foots[6].string = str(self.cxty.total)
        foots[7].string = str(self.lines.missed)
        foots[8].string = str(self.lines.total)
        foots[9].string = str(self.methods.missed)
        foots[10].string = str(self.methods.total)
        if not self.is_page_for_class():
            foots[11].string = str(self.classes.missed)
            foots[12].string = str(self.classes.total)

    def is_page_for_class(self):
        return not self._fullpath.endswith('index.html')

    def exclude(self, excludes):
        to_excludes = set([])
        for element in self.childs:
            if element.name in excludes:
                element.decompose()
                to_excludes.add(element)
        self.childs.difference_update(to_excludes)
        return self

    def _load(self):
        with codecs.open(self._fullpath, mode='rb', encoding='utf-8') as input_file:
            self._soup = BeautifulSoup(input_file.read(), 'html.parser')
            self._name = self._soup.h1.text
            ## parse metrics
            metrics_element = self._soup.tfoot.find_all('td')
            metrics = flatten([m.text.replace(',','').split('of') for m in metrics_element])
            ## [u'Total', u'673501 ', u' 1023983', u'34%', u'59753 ', u' 82034', u'27%', u'49976', u'68755', u'128281', u'201772', u'14542', u'27312', u'1614', u'3883']
            self.instructions.missed = metrics[1]
            self.instructions.total = metrics[2]
            self.branches.missed = metrics[4]
            self.branches.total = metrics[5]
            self.cxty.missed = metrics[7]
            self.cxty.total = metrics[8]
            self.lines.missed = metrics[9]
            self.lines.total = metrics[10]
            self.methods.missed = metrics[11]
            self.methods.total = metrics[12]

            if not self.is_page_for_class():
                self.classes.missed = metrics[13]
                self.classes.total = metrics[14]
                # parse child
                for line in self._soup.tbody.find_all('tr'):
                    path = '%s/%s' % (os.path.dirname(self._fullpath), line.a.get('href'))
                    item = Element(path, line)
                    self.childs.add(item)

class Index(object):
    def __init__(self, fullpath, exclude_packages=EXCLUDE_PACKAGES,
            exclude_classes=EXCLUDE_CLASSES):
        self._fullpath = fullpath
        self._root = Element(fullpath)
        self._exclude_packages = exclude_packages
        self._exclude_classes = exclude_classes

    @property
    def root(self):
        return self._root

    def clean(self):
        """ use dfs to clean up """
        self._root.exclude(self._exclude_packages)
        stack = [self._root]
        while stack:
            current = stack.pop()
            if current.name in self._exclude_classes:
                current.exclude(self._exclude_classes[current.name])
            for child in current.childs:
                stack.append(child)

    def refresh(self):
        """ use bfs to refresh from leaves to root"""
        levels = [[self._root]]
        ## build levels
        while True:
            current_level = levels[-1]
            next_level = []
            for element in current_level:
                next_level.extend(element.childs)
            levels.append(next_level)
            if next_level == []:
                break

        ## refresh
        while levels:
            current_level = levels.pop()
            for element in current_level:
                element.rebuild_metrics()
                element.flush_to_disk()



def main():
    index = Index(ROOT + "index.html")
    index.clean()
    index.refresh()

if __name__ == "__main__":
    main()
