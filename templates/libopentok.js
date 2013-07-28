window.opentok = {
    session: null,
    params: null,

    isPhone: function() {
      if(this.params.phone == 'true')
        return true;
      return false;
    },

    editUI: function() {

    },

    init: function() {
      this.params = function () {
          // This function is anonymous, is executed immediately and 
          // the return value is assigned to QueryString!
          var query_string = {};
          var query = window.location.search.substring(1);
          var vars = query.split("&");
          for (var i=0;i<vars.length;i++) {
            var pair = vars[i].split("=");
              // If first entry with this name
            if (typeof query_string[pair[0]] === "undefined") {
              query_string[pair[0]] = pair[1];
              // If second entry with this name
            } else if (typeof query_string[pair[0]] === "string") {
              var arr = [ query_string[pair[0]], pair[1] ];
              query_string[pair[0]] = arr;
              // If third or later entry with this name
            } else {
              query_string[pair[0]].push(pair[1]);
            }
          } 
            return query_string;
        } ();


      var self = this;
      this.apikey = '36524892';
      this.session_id = "2_MX4zNjUyNDg5Mn4xMjcuMC4wLjF-U3VuIEp1bCAyOCAwMjowMDoxMiBQRFQgMjAxM34wLjQ0NzQzNjd-";
      
      
      this.token = 'T1==cGFydG5lcl9pZD0zNjUyNDg5MiZzZGtfdmVyc2lvbj10YnJ1YnktdGJyYi12MC45MS4yMDExLTAyLTE3JnNpZz00YTY4N2MwZmYxMjQ5MmMxZDk3NWUwYmYwZTY0MmM5ZTJhMGQzYTliOnJvbGU9cHVibGlzaGVyJnNlc3Npb25faWQ9Ml9NWDR6TmpVeU5EZzVNbjR4TWpjdU1DNHdMakYtVTNWdUlFcDFiQ0F5T0NBd01qb3dNRG94TWlCUVJGUWdNakF4TTM0d0xqUTBOelF6TmpkLSZjcmVhdGVfdGltZT0xMzc1MDAyMTQyJm5vbmNlPTAuNDEzMzc5MzA1ODI3MzgzMzYmZXhwaXJlX3RpbWU9MTM3NzU5NDE0MiZjb25uZWN0aW9uX2RhdGE9';
      this.session = TB.initSession(self.session_id);

      var subscribeToStreams = function(event) {
        var streams = event.streams;
        
        for (var i = 0; i < streams.length; i++) {
          var stream = streams[i];
          if (stream.connection.connectionId != event.target.connection.connectionId) {
            self.session.subscribe(stream, getStreamDiv(stream), { width: 500, height: 500 } );
          }
        }
      }
      
      var getStreamDiv = function(stream) {
        var div = document.createElement('div');
        var name = 'video_chat_stream_' + stream.streamId;
        div.setAttribute('id', name);

        var streamsContainer = document.getElementById('video_chat_container');
        streamsContainer.appendChild(div);

        return name;
      }
      
      var sessionConnectedHandler = function(event) {
        var publisher = TB.initPublisher(self.apikey, 'video_chat_self');
        subscribeToStreams(event);
        self.session.publish(publisher);
      }
      
      var streamCreatedHandler = function(event) {
        subscribeToStreams(event);
      }
      
      this.session.addEventListener('sessionConnected', sessionConnectedHandler);
      this.session.addEventListener("streamCreated", streamCreatedHandler);
      
      this.session.connect(self.apikey, self.token);
      
    }
  }