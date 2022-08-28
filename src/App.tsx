import React from 'react';
import './App.css';

const d3 = require("d3")

export default class App extends React.Component<{}, {}> {

  componentDidMount() {
    var svg = d3.select("svg"),
      margin = 200,
      width = svg.attr("width") - margin,
      height = svg.attr("height") - margin;

    console.log(svg)

    svg.append("text")
      .attr("transform", "translate(100,0)")
      .attr("x", 50)
      .attr("y", 50)
      .attr("font-size", "24px")
      .text("XYZ Foods Stock Price")

    const chart = d3.IndexChart("", {
      
    })

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
