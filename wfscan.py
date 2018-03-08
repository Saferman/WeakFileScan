import requests
import base64
import random
import argparse


def get_headers():
    # cookie = ''
    user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
                  'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60',
                  'Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
    UA = random.choice(user_agent)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': UA,
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'Cookie': cookie
    }
    return headers


def random_str():
    key = random.random() * 100
    return base64.b64encode(str(key).encode()).decode().replace('=', '')


def file_scan(url):
    ran_str = random_str()
    headers = get_headers()
    dirs = []
    payloads = ["/robots.txt", "/README.md", "/crossdomain.xml", "/.git/config", "/.svn/entries", "/.svn/wc.db",
                "/.DS_Store", "/CVS/Root", "/CVS/Entries", "/.idea/workspace.xml"]
    payloads += ["/index.htm", "/index.html", "/index.php", "/index.asp", "/index.aspx", "/index.jsp", "/index.do",
                 "/index.action", "/index.phps", "/index.php~", "/.index.php", "/index.php.bak"]
    payloads += ["/www/", "/console", "/web-console", "/web_console", "/jmx-console", "/jmx_console",
                 "/JMXInvokerServlet", "/invoker"]
    payloads += ["/index.bak", "/index.swp", "/index.old", "/.viminfo", "/.bash_history", "/.bashrc",
                 "/project.properties", "/config.properties", "/config.inc", "/common.inc", "/db_mysql.inc",
                 "/install.inc", "/conf.inc", "/db.inc", "/setup.inc", "/init.inc", "/config.ini", "/php.ini",
                 "/info.ini", "/setup.ini", "/www.ini", "/http.ini", "/conf.ini", "/core.config.ini", "/ftp.ini",
                 "/data.mdb", "/db.mdb", "/test.mdb", "/database.mdb", "/Database.mdf", "/BookStore.mdf", "/DB.mdf"]
    payloads += ["/1.sql", "/install.sql", "/schema.sql", "/mysql.sql", "/dump.sql", "/users.sql", "/update.sql",
                 "/test.sql", "/user.sql", "/database.sql", "/sql.sql", "/setup.sql", "/init.sql", "/login.sql",
                 "/backup.sql", "/all.sql", "/passwd.sql", "/init_db.sql"]
    payloads += ["/fckstyles.xml", "/Config.xml", "/conf.xml", "/build.xml", "/web.xml", "/test.xml", "/ini.xml",
                 "/www.xml", "/db.xml", "/database.xml", "/admin.xml", "/login.xml", "/sql.xml", "/sample.xml",
                 "/settings.xml", "/setting.xml", "/info.xml", "/install.xml", "/php.xml", "/.mysql_history"]
    payloads += ["/nginx.conf", "/httpd.conf", "/test.conf", "/conf.conf", "/local.conf", "/user.txt", "/LICENSE.txt",
                 "/sitemap.xml", "/username.txt", "/pass.txt", "/passwd.txt", "/password.txt", "/.htaccess",
                 "/web.config", "/app.config", "/log.txt", "/config.xml", "/CHANGELOG.txt", "/INSTALL.txt",
                 "/error.log"]
    payloads += ["/login", "/phpmyadmin", "/pma", "/pmd", "/SiteServer", "/admin", "/Admin/", "/manage", "/manager",
                 "/manage/html", "/resin-admin", "/resin-doc", "/axis2-admin", "/admin-console", "/system", "/wp-admin",
                 "/uc_server", "/debug", "/Conf", "/webmail", "/service", "/ewebeditor"]
    payloads += ["/xmlrpc.php", "/search.php", "/install.php", "/admin.php", "/regist.php", "/login.php", "/l.php",
                 "/phpinfo.php", "/info.php", "/setup.php", "/forum.php", "/sql.php", "/flag.php", "/getflag.php"]
    payloads += ["/portal", "/blog", "/bbs", "/webapp", "/webapps", "/plugins", "/cgi-bin", "/htdocs", "/wsdl", "/html",
                 "/install", "/test", "/tmp", "/file", "/solr/#/", "/WEB-INF", "/zabbix", "/backup", "/log", "/test"]
    payloads += ["/www.7z", "/www.rar", "/www.zip", "/www.tar.gz", "/wwwroot.zip", "/wwwroot.rar", "/wwwroot.7z",
                 "/wwwroot.tar.gz", "/backup.7z", "/backup.rar", "/backup.tar", "/backup.tar.gz", "/backup.zip",
                 "/index.7z", "/index.rar", "/index.sql", "/index.tar", "/index.tar.gz", "/index.zip"]
    if url[-1:] == '/':
        url = url[:-1]
    try:
        check_url = url + '/' + ran_str
        print('[*] Now is check waf: ' + check_url)
        check_waf = requests.get(check_url, verify=True, timeout=3)
        for payload in payloads:
            try:
                req = requests.get(url + payload, verify=True, timeout=3)
                if req.status_code == 200 and abs(len(check_waf.text) - 10 - len(req.text)) > 10:
                    print('[+] Get %s 200' % (url+payload))
                    dirs.append(payload)
            except:
                pass
    except:
        pass
    if len(dirs) > 40:
        print('[*] Maybe Got waf.')
        return '[]'
    else:
        return dirs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", action="store", help="Target URL (e.g. 'http://www.site.com')")
    group.add_argument("-l", "--list", action="store", help="URL list file (e.g. 'targets.txt')")
    args = parser.parse_args()
    if args.url:
        result = file_scan(args.url)
        print(result)
    elif args.list:
        result = {}
        filename = args.list
        with open(filename) as f:
            for line in f:
                line = line.rstrip("\n")
                _result = file_scan(line)
                result[line] = _result
        for key in result:
            print('[+] ' + key)
            print('[+] ' + str(result[key]))
    else:
        print("error: missing a mandatory option (-u or -l), use -h for basic help")
