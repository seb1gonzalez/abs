-- TimedScreenshots frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
TimedScreenshots_proto = Proto("timedscreenshots","TimedScreenshots Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("timedscreenshots.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("timedscreenshots.data","Log Data")

-- add the field to the protocol
TimedScreenshots_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function TimedScreenshots_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1604606461.0 and pinfo.abs_ts <= 1604606463.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1604606461.0876677_screenshot.png")

       subtree:add(timestamp_F,tostring("2020-11-05T20:01:01"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(TimedScreenshots_proto)