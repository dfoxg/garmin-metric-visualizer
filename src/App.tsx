import React from 'react';
import './App.css';

const d3 = require("d3")

export default class App extends React.Component<{}, {}> {

  componentDidMount() {
    var svg = d3.select("svg"),
      margin = 200,
      width = svg.attr("width") - margin,
      height = svg.attr("height") - margin;

    var data = [{ x: 0, y: 0 }, { x: 150, y: 150 }, { x: 300, y: 100 }, { x: 450, y: 30 }, { x: 600, y: 130 }]

    var curveFunc = d3.line()
      .curve(d3.curveBasis)
      .x(function (d: any) { return d.x })
      .y(function (d: any) { return d.y })

    svg.append('path')
      .attr('d', curveFunc(data))
      .attr('stroke', 'black')
      .attr('fill', 'none');


    svg.append("text")
      .attr("transform", "translate(100,0)")
      .attr("x", 50)
      .attr("y", 30)
      .attr("font-size", "24px")
      .text("Here should come the graphs")

  }

  handleFileChange(event: React.ChangeEvent<HTMLInputElement>): any {
    const file = event.target.files![0]
    file.text().then(data => {
      console.log(JSON.parse(data))
    })
  }

  render(): React.ReactNode {
    return (
      <div className="App">
        <header className="App-header">
          <span>Garmin Metric Visualizer</span>
        </header>
        <div className='content'>
          <p>
            Please upload a file &nbsp;
            <input id="file_select" type={'file'} onChange={(event) => { this.handleFileChange(event) }} accept=".json" multiple={false}></input>
          </p>
          <svg className='d3_output'>
          </svg>
        </div>
      </div>
    )
  }
}
