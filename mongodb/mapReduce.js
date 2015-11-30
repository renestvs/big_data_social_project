var mapFunction = function() {
		var timeStamp = this.created_at;
		var key = "";
		timeStamp = timeStamp.split(" ");
		var data = timeStamp[2]+timeStamp[1]+timeStamp[5];
		var hashtags = this.entities.hashtags;
		for (var i = 0; i < hashtags.length; i++) {
			hash = hashtags[i].text.toLowerCase();
			key = data+"_"+hash;
			emit(key, 1);
		}
    };

var reduceFunction = function(key, values){
		return Array.sum( values );
	}

var mapFunction = function() {
		var key = "";
		var hashtags = this.entities.hashtags;
		for (var i = 0; i < hashtags.length; i++) {
			hash = hashtags[i].text.toLowerCase();
			key = hash;
			emit(key, 1);
		}
    };

var reduceFunction = function(key, value){
		return Array.sum( value );
	}


var map = function(){
	var id = this.id_str;
	var mentions = this.entities.user_mentions;
	for(i = 0; i < mentions.length; i++)
	{
		cmp_key = id+" "+mentions[i].id_str;
		var value = {"from" : id, "to" : mentions[i].id_str, "weight": 1};
		emit(cmp_key, value);
	}
};

var reduce = function(key, values){
	var r_values = values.length;
	var ids = key.split("_");
	var cmp_values = {"from" : ids[0], "to" : ids[1], "weight" : r_values};
	return(cmp_values);
}