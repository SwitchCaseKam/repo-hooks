#!/usr/bin/env python 
import sys, re

def main():
    commit_msg = sys.argv[1] 
    commit_msg_array=commit_msg.split('\n');
    commit_msg_array=[line for line in commit_msg_array if line != '']

    full_header = commit_msg_array[0]
    header_tag = get_commit_header_tag(full_header)
    if (header_tag != None):
        if (header_tag == 'none'):
            print('Commit message: OK')
            return 0
        else: 
            description = commit_msg_array[1]
            feature_id = commit_msg_array[2]
            jira_id = commit_msg_array[3]
            return check_commit_footer_feature_id(feature_id, full_header)
    else:
        print('ERROR: commit message not compliant with requriements')
        return 1;

def get_commit_header_tag(header):
    header_regex = re.search('^\[(.*)\] ', header)
    if (header_regex != None):
        return header_regex.group(1)
    else:
        return None;

def check_commit_header(header):
    header_regex = re.search('^\[(.*)\] ' ,header)
    if (header_regex != None):
        header_tag = header_regex.group(1)
        print('Commit header: OK')
        return 0;
    else:
        print('ERROR with header commit tag')
        return 1;

def check_commit_footer_feature_id(feature_id, header):
    header_tag = get_commit_header_tag(header)
    feature_regex = re.search('=(.*)' , feature_id)
    if (feature_regex != None):
        feature_id = feature_regex.group(1)
        if (header_tag == feature_id ):
            print('Commit footer: OK ')
            return 0
        else:
            print('ERROR: footer id is not compliant with commit header tag')
            return 1
    else:
        print('ERR: footer id is not compliant with commit header tag')
        return 1
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
