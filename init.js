"use strict";

(
  function(exports) {
          exports.name = "mynd";
          exports.margin = 60;
          exports.width = 1000 - exports.margin;
          exports.height = 600 - exports.margin;

          exports.radius = 3;
          exports.aldursflokkar = ['30 ára-','30-37 ára','38-54 ára','55-59 ára','60 ára+'];

          exports.teikniflotur = d3.select("#teikniflotur1")
            .append("svg")
            .attr("width", exports.width + exports.margin)
            .attr("height", exports.height + exports.margin)
            .append('g')
            .attr('class','chart');

          exports.percentage_scale = d3.scale.linear()
              .range([exports.height, exports.margin])
              .domain([-5,120]);

          exports.percentage_axis = d3.svg.axis()
            .scale(exports.percentage_scale)
            .orient("left")
            .ticks(10);

          exports.teikniflotur
            .append("g")
            .attr("class", "y axis")
            .attr("transform", "translate(" + exports.margin + ",0)")
            .call(exports.percentage_axis);

         
          // ordinal axis
          exports.ordinal_scale = d3.scale.ordinal()
          .rangePoints([exports.margin, exports.width-exports.margin])
          .domain(['','Stærðfræði','Tungumál','Félagsgreinar','Íslenska','Raungreinar']);
          

          exports.ordinal_axis = d3.svg.axis()
            .scale(exports.ordinal_scale)
            .orient("bottom");


          exports.teikniflotur
            .append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + (exports.height-23) + ")")
            .call(exports.ordinal_axis);
          

          exports.right_header = exports.teikniflotur.append("g")
              .attr("class", "right_header")
              .attr("transform", "translate(" + exports.width + "," + (exports.height/3) + ")")
              .append('text')
              .text('Fjöldi ' + 15)
              .attr('font-size','20px'); 

          exports.right_header2 = exports.teikniflotur.append("g")
              .attr("class", "right_header2")
              .attr("transform", "translate(" + exports.width + "," + (exports.height/3 + 30) + ")")
              .append('text')
              .text('Hópar ' + 4)
              .attr('font-size','20px'); 

          exports.header = exports.teikniflotur.append("g")
              .attr("class", "header")
              .attr("transform", "translate(" + (exports.width/3) + "," + 40 + ")")
              .selectAll("g")
              .data(['Launavöxtur í % síðan 2013'])
              .enter().append("g");

          exports.header.append("text")
              .text(function(d) {
                return d;
            })
            .attr('font-size','24px'); 

          exports.legend = exports.teikniflotur.append("g")
              .attr("class", "legend")
              .attr("transform", "translate(" + exports.width + "," + 20 + ")")
              .selectAll("g")
              .data(['30 ára-','30-37 ára','38-54 ára','55-59 ára','60 ára+'])
              .enter().append("g");

          exports.legend.append("rect")
              .attr('width','10')
              .attr('height','10')
              .attr('y', function(d,i) {
                return i*100/5 + 40;
              })
              .style('fill',function(d,i) {
                var aldurslitir = ["#d7191c","#fdae61","#ffffbf","#abd9e9","#2c7bb6"];
                return aldurslitir[i];
            });
          
          exports.legend.append("text")
              .attr("x",20)
              .attr("y", function(d,i) {
                return i*100/5 + 50;
              })
              .text(function(d) {
                  return d;
            });
          exports.lineFunction = d3.svg.line()
                          .x(function(d) { return d.x; })
                          .y(function(d) { return d.y; })
                         .interpolate("linear");

            for (var i = 0; i < 12; i++) {
              exports.lineData = [ { "x": 60,   "y": 60 + i*38.45},  { "x": exports.width-10,  "y": 60+i*38.45}];
              exports.lineGraph = exports.teikniflotur.append("path")
                            .attr('class','line')
                            .attr("d", exports.lineFunction(exports.lineData))
                            
              }
          exports.x = function(d) {
               
                  var r = exports.ordinal_scale(d['synidaemi']); 
                  if (d['aldursflokkur'] == '60 ára+')
                    return r;
                  else if (d['aldursflokkur'] == '55-59 ára')
                    return r-20;
                  else if (d['aldursflokkur'] == '38-54 ára')
                    return r-30;
                  else if (d['aldursflokkur'] == '30-37 ára')
                    return r-40;
                  else
                    return r -50;

          }
          exports.tooltipFunction = function(tooltip,data,id,item) {
              
              var item = data.filter(d=> d.key == id)[0];
              tooltip[0][0].innerHTML = "Sýnidæmi: " + item.synidaemi + "<br>Mismunur: " + parseInt(item.mismunur1) + "%<br>";
              tooltip[0][0].innerHTML += "Launaflokkur: " + item.launaflokkur +", þrep: " + item.threp + "<br>";
              tooltip[0][0].innerHTML += "Laun: " + parseFloat(item.laun).toFixed(0) + "<br>";
              if (item.synidaemi != "2013") {
                tooltip[0][0].innerHTML += "Vinnumat: " + parseFloat(item.vinnumat).toFixed(0) + "<br>";
                tooltip[0][0].innerHTML += (item.skertur == "True" ? "Skert vinnumat": "Óskert vinnumat");

              }
              else {
                tooltip[0][0].innerHTML += "Kennsluskylda: " + item.kennsluskylda;

              }
              return tooltip.style("visibility", "visible");
            };
          exports.pr_scale = function(d) {
              return this.percentage_scale(d['mismunur1']);
            };
})(this.mynd = {})
