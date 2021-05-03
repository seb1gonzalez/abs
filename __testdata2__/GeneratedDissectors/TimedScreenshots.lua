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
    if pinfo.abs_ts >= 1620036808.0 and pinfo.abs_ts <= 1620036810.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036808.9640083_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:28"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036817.0 and pinfo.abs_ts <= 1620036819.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036817.139567_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:37"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036839.0 and pinfo.abs_ts <= 1620036841.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036839.471791_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:59"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036761.0 and pinfo.abs_ts <= 1620036763.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036761.1689768_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:41"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036774.0 and pinfo.abs_ts <= 1620036776.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036774.4732382_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:54"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036731.0 and pinfo.abs_ts <= 1620036733.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036731.5605612_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:11"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036799.0 and pinfo.abs_ts <= 1620036801.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036799.2694037_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:19"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036711.0 and pinfo.abs_ts <= 1620036713.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036711.4107733_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:51"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036785.0 and pinfo.abs_ts <= 1620036787.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036785.852715_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:05"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036810.0 and pinfo.abs_ts <= 1620036812.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036810.3360512_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:30"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036813.0 and pinfo.abs_ts <= 1620036815.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036813.006591_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:33"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036800.0 and pinfo.abs_ts <= 1620036802.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036800.642771_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036857.0 and pinfo.abs_ts <= 1620036859.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036857.6756759_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:17"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036768.0 and pinfo.abs_ts <= 1620036770.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036768.2102587_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:48"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036762.0 and pinfo.abs_ts <= 1620036764.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036762.5635054_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:42"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036723.0 and pinfo.abs_ts <= 1620036725.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036723.2195568_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:03"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036788.0 and pinfo.abs_ts <= 1620036790.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036788.5727077_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:08"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036735.0 and pinfo.abs_ts <= 1620036737.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036735.0918534_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:15"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036730.0 and pinfo.abs_ts <= 1620036732.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036730.1671457_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:10"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036759.0 and pinfo.abs_ts <= 1620036761.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036759.761459_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:39"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036721.0 and pinfo.abs_ts <= 1620036723.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036721.781832_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:01"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036795.0 and pinfo.abs_ts <= 1620036797.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036795.1755724_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:15"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036783.0 and pinfo.abs_ts <= 1620036785.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036783.2099018_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:03"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036806.0 and pinfo.abs_ts <= 1620036808.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036806.1406221_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:26"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036775.0 and pinfo.abs_ts <= 1620036777.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036775.8781228_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:55"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036763.0 and pinfo.abs_ts <= 1620036765.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036763.9467766_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:43"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036849.0 and pinfo.abs_ts <= 1620036851.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036849.0724816_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:09"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036860.0 and pinfo.abs_ts <= 1620036862.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036860.4049828_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036780.0 and pinfo.abs_ts <= 1620036782.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036780.2748332_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:00"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036850.0 and pinfo.abs_ts <= 1620036852.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036850.7733657_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:10"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036854.0 and pinfo.abs_ts <= 1620036856.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036854.9125962_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:14"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036714.0 and pinfo.abs_ts <= 1620036716.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036714.7567568_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:54"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036778.0 and pinfo.abs_ts <= 1620036780.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036778.835319_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:58"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036846.0 and pinfo.abs_ts <= 1620036848.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036846.3203366_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:06"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036716.0 and pinfo.abs_ts <= 1620036718.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036716.1481156_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:56"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036814.0 and pinfo.abs_ts <= 1620036816.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036814.3957055_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:34"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036789.0 and pinfo.abs_ts <= 1620036791.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036789.9848506_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:09"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036773.0 and pinfo.abs_ts <= 1620036775.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036773.0351648_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:53"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036728.0 and pinfo.abs_ts <= 1620036730.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036728.7757654_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:08"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036856.0 and pinfo.abs_ts <= 1620036858.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036856.2889204_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036833.0 and pinfo.abs_ts <= 1620036835.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036833.509396_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:53"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036862.0 and pinfo.abs_ts <= 1620036864.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036862.2229736_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036843.0 and pinfo.abs_ts <= 1620036845.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036843.5805538_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:03"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036771.0 and pinfo.abs_ts <= 1620036773.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036771.1587512_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:51"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036842.0 and pinfo.abs_ts <= 1620036844.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036842.1946526_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:02"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036815.0 and pinfo.abs_ts <= 1620036817.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036815.7554553_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:35"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036718.0 and pinfo.abs_ts <= 1620036720.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036718.9733322_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:58"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036840.0 and pinfo.abs_ts <= 1620036842.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036840.853827_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:00"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036802.0 and pinfo.abs_ts <= 1620036804.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036802.0309083_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:22"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036818.0 and pinfo.abs_ts <= 1620036820.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036818.5430837_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:38"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036797.0 and pinfo.abs_ts <= 1620036799.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036797.8996105_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:17"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036736.0 and pinfo.abs_ts <= 1620036738.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036736.4421115_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036852.0 and pinfo.abs_ts <= 1620036854.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036852.1588812_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036787.0 and pinfo.abs_ts <= 1620036789.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036787.257656_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:07"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036732.0 and pinfo.abs_ts <= 1620036734.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036732.9722075_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036717.0 and pinfo.abs_ts <= 1620036719.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036717.509964_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:11:57"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036769.0 and pinfo.abs_ts <= 1620036771.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036769.6485944_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:49"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036819.0 and pinfo.abs_ts <= 1620036821.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036819.9120445_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:39"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036796.0 and pinfo.abs_ts <= 1620036798.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036796.5300002_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:16"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036720.0 and pinfo.abs_ts <= 1620036722.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036720.4018729_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:00"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036726.0 and pinfo.abs_ts <= 1620036728.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036726.0290442_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:06"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036765.0 and pinfo.abs_ts <= 1620036767.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036765.3507216_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:45"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036826.0 and pinfo.abs_ts <= 1620036828.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036826.5747578_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:46"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036766.0 and pinfo.abs_ts <= 1620036768.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036766.7965937_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:46"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036777.0 and pinfo.abs_ts <= 1620036779.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036777.402231_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:57"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036724.0 and pinfo.abs_ts <= 1620036726.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036724.6365306_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:04"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036803.0 and pinfo.abs_ts <= 1620036805.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036803.405754_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:23"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036792.0 and pinfo.abs_ts <= 1620036794.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036792.7191994_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:12"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036853.0 and pinfo.abs_ts <= 1620036855.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036853.532552_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:13"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036847.0 and pinfo.abs_ts <= 1620036849.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036847.6665049_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:07"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036804.0 and pinfo.abs_ts <= 1620036806.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036804.7630043_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:24"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036859.0 and pinfo.abs_ts <= 1620036861.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036859.0461302_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:19"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036727.0 and pinfo.abs_ts <= 1620036729.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036727.4105809_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:12:07"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036781.0 and pinfo.abs_ts <= 1620036783.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036781.7662566_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:01"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036811.0 and pinfo.abs_ts <= 1620036813.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036811.6598637_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:31"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036807.0 and pinfo.abs_ts <= 1620036809.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036807.5607014_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:27"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036844.0 and pinfo.abs_ts <= 1620036846.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036844.9761717_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:14:04"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1620036791.0 and pinfo.abs_ts <= 1620036793.0 then
       local subtree = tree:add(TimedScreenshots_proto,"TimedScreenshots Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1620036791.3894167_screenshot.png")

       subtree:add(timestamp_F,tostring("2021-05-03T10:13:11"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(TimedScreenshots_proto)