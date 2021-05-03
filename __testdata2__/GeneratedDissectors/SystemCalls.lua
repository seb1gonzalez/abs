-- SystemCalls frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
SystemCalls_proto = Proto("systemcalls","SystemCalls Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("systemcalls.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("systemcalls.data","Log Data")

-- add the field to the protocol
SystemCalls_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function SystemCalls_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1620036716.0 and pinfo.abs_ts <= 1620036718.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("whoami")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:56"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036730.0 and pinfo.abs_ts <= 1620036732.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sudo ifconfig")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:10"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036732.0 and pinfo.abs_ts <= 1620036734.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("ifconfig")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("msfconsole /usr/share/metasploit-framework/ruby /usr/bin/msfconsole")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("egrep /usr/bin/egrep -q /usr/share/metasploit-framework/vendor/bundle")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("grep -E -q /usr/share/metasploit-framework/vendor/bundle")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("ruby /usr/bin/msfconsole")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036737.0 and pinfo.abs_ts <= 1620036739.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c git --version > /dev/null 2>&1")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:17"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036737.0 and pinfo.abs_ts <= 1620036739.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("git --version")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:17"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036748.0 and pinfo.abs_ts <= 1620036750.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("hostname")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:28"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036756.0 and pinfo.abs_ts <= 1620036758.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("office365useren python3 /usr/share/metasploit-framework/modules/auxiliary/gather/office365userenum.py")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036756.0 and pinfo.abs_ts <= 1620036758.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("python3 /usr/share/metasploit-framework/modules/auxiliary/gather/office365userenum.py")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("infocmp -C")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("infocmp -C -r")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("infocmp -C -r")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty size")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("infocmp -C -r")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036757.0 and pinfo.abs_ts <= 1620036759.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -g")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -a")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036816.0 and pinfo.abs_ts <= 1620036818.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty -echo -icrnl cbreak pass8 -ixoff")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036819.0 and pinfo.abs_ts <= 1620036821.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sh -c stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:39"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036819.0 and pinfo.abs_ts <= 1620036821.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("stty 4100:5:bf:8a3b:3:1c:8:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:39"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036841.0 and pinfo.abs_ts <= 1620036843.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("git clone https://github.com/javanikeed/business_data.git")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:01"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036844.0 and pinfo.abs_ts <= 1620036846.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("ls clone")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:04"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036856.0 and pinfo.abs_ts <= 1620036858.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("cat sensitive_passwords.txt")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036860.0 and pinfo.abs_ts <= 1620036862.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("df -h")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("service /usr/sbin/service auditd stop")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("basename /usr/sbin/service")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("basename /usr/sbin/service")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("systemctl --quiet is-active multi-user.target")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("systemctl list-unit-files --full multi-user.target")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("sed -ne s/.sockets*[a-z]*s*$/.socket/p")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("xhost -SI:localuser:root")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("auditd_parser.s bash /home/kali/eceld-netsys/eceld/plugins/parsers/auditd/auditd_parser.sh /home/kali/eceld-netsys/eceld/plugins/collectors/auditd/raw /home/kali/eceld-netsys/eceld/plugins/collectors/auditd/parsed")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("bash /home/kali/eceld-netsys/eceld/plugins/parsers/auditd/auditd_parser.sh /home/kali/eceld-netsys/eceld/plugins/collectors/auditd/raw /home/kali/eceld-netsys/eceld/plugins/collectors/auditd/parsed")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(SystemCalls_proto,"SystemCalls Log")
       local mycomplientstr = tostring("cat /home/kali/eceld-netsys/eceld/plugins/collectors/auditd/raw/1620036709_auditd.txt")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(SystemCalls_proto)