# XOOMSetterGetter
This code will generate setter and getter in Swift 2.3 function from your class properties (java). I know it sounds awkward, but it will help you! Alot!

 > Copy-paste FTW using XOOM 

Xoom is just personal framework for developing iOS application based on android's code! Yeah, you read it right. All you need to do is just copy and paste! - meh

## Requirement
- Python 2.7
- Your java code

## How to use
1. Clone this repo `$git clone https://github.com/riyanpratama/XOOMSetterGetter.git`
2. Go into your folder, there are three files you need to know. First, **setget.py** the main file, **input.txt** as input file, and **output.txt** that you would copyy for your project.
3. Copy your class properties (java), e.g.
	```
	public Date StartPeriod;
	
	public Date EndPeriod;
	
	public String CoverageType;
	```
4. Paste into your **input.txt**
5. Run `$python setget.py`, and just it. 
6. Open your **output.txt**, you can use any text editor or just `$cat output.txt` in your terminal.
	```
	public var StartPeriod: Date!
	public var EndPeriod: Date!
	public var CoverageType: String!

	public func setStartperiod(startPeriod: Date) { 
		self.StartPeriod = startPeriod
	}

	public func setEndperiod(endPeriod: Date) { 
		self.EndPeriod = endPeriod
	}

	public func setCoveragetype(coverageType: String) { 
		self.CoverageType = coverageType
	}


	public func getStartperiod() -> Date {
		return StartPeriod
	}

	public func getEndperiod() -> Date {
		return EndPeriod
	}

	public func getCoveragetype() -> String {
		return CoverageType
	}

	```
7. That's all you need! Copy and Paste into your class! 

## Disclaimer
Personal use only. Due to our beloved XOOM. 

**P.S** Your developer, WUP. *kiss*
