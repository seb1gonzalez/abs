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
    if pinfo.abs_ts >= 1604606460.0 and pinfo.abs_ts <= 1604606462.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Control_L][Shift_L]Twget google.com[Return]wget amazon.com[Return]whoami[Return]exit[Return][Alt_L]")

       subtree:add(timestamp_F,tostring("2020-11-05T20:01:00"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(Keypresses_proto)