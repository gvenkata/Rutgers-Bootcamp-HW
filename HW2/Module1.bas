Attribute VB_Name = "Module1"
Option Explicit

Sub Summarize_Ticker()
Dim Current As Worksheet
Dim pop_rows As Long
Dim pop_rows2 As Long

Dim i As Long

Dim ticker As String
Dim tot_vol As Double
Dim Summary_Table_Row As Integer


Dim yr_open As Double
Dim yr_close As Double
Dim vChange As Double

Dim vDec As Double
Dim vInc As Double
Dim vTot As Double
Dim vTick1 As String
Dim vTick2 As String
Dim vTick3 As String


Call Module2.OptimizeCode_Begin

    For Each Current In Worksheets
    
        Current.Activate
        
        pop_rows = Range("A1").End(xlDown).Row
        
 
        Cells(1, 9).Value = "Ticker" 'I
        Cells(1, 10).Value = "Yearly Change" 'J
        Cells(1, 11).Value = "Percent Change" 'K 11
        Cells(1, 12).Value = "Total Stock Volume" 'L 12
        
        Cells(2, 15).Value = "Greatest % Increase"
        Cells(3, 15).Value = "Greatest % Decrease"
        Cells(4, 15).Value = "Greatest Total Volume"
        Cells(1, 16).Value = "Ticker"
        Cells(1, 17).Value = "Value"
        
        Summary_Table_Row = 2
        
        
        'populate ticker and total volume (col I and L)
        ' col 3 open, col 6 close
    
        For i = 2 To pop_rows
        
            If Cells(i, 1).Value <> Cells(i - 1, 1).Value Then
                ' capture open
                 yr_open = Cells(i, 3).Value
            End If
            
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                ticker = Cells(i, 1).Value
                tot_vol = tot_vol + Cells(i, 7).Value
                yr_close = Cells(i, 6).Value
                
                Range("I" & Summary_Table_Row).Value = ticker
                Range("J" & Summary_Table_Row).Value = yr_close - yr_open
                
                If yr_open <> 0 Then
                'Range("K" & Summary_Table_Row).Value = FormatPercent(((yr_close - yr_open) / (yr_open)), 2)
                Range("K" & Summary_Table_Row).Value = (yr_close - yr_open) / (yr_open)
                ElseIf yr_open = 0 And yr_close <> 0 Then
                'Range("K" & Summary_Table_Row).Value = FormatPercent(((yr_close - 1) / (1)), 2)
                Range("K" & Summary_Table_Row).Value = (yr_close - 1) / (1)
                Range("M" & Summary_Table_Row).Value = "**opening of 0 set to 1 to calculate increase**"
                ElseIf yr_open = 0 And yr_close = 0 Then
                'Range("K" & Summary_Table_Row).Value = FormatPercent(((yr_close - 1) / (1)), 2)
                Range("K" & Summary_Table_Row).Value = 0
                Range("M" & Summary_Table_Row).Value = "**open and close were 0**"
                End If
                
                If (yr_close - yr_open) > 0 Then
                    Range("J" & Summary_Table_Row).Interior.Color = vbGreen
                End If
                
                If (yr_close - yr_open) < 0 Then
                    Range("J" & Summary_Table_Row).Interior.Color = vbRed
                End If
                
                
                Range("L" & Summary_Table_Row).Value = tot_vol
                Summary_Table_Row = Summary_Table_Row + 1
                tot_vol = 0
            Else
                tot_vol = tot_vol + Cells(i, 7).Value
            End If
            
           
        Next i
        
        pop_rows2 = Range("I1").End(xlDown).Row
        
        vDec = Cells(2, 11).Value
        vInc = Cells(2, 11).Value
        vTot = Cells(2, 12).Value
        vTick1 = Cells(2, 9).Value
        vTick2 = Cells(2, 9).Value
        vTick3 = Cells(2, 9).Value
        
        For i = 2 To pop_rows2
        
        'get min, set ticker
        If Cells(i + 1, 11).Value < vDec Then
        vDec = Cells(i + 1, 11).Value
        vTick1 = Cells(i + 1, 9).Value
        End If
        
        'get max, set ticker
        If Cells(i + 1, 11).Value > vInc Then
        vInc = Cells(i + 1, 11).Value
        vTick2 = Cells(i + 1, 9).Value
        End If
        
        'get total, set ticker
        If Cells(i + 1, 12).Value > vTot Then
        vTot = Cells(i + 1, 12).Value
        vTick3 = Cells(i + 1, 9).Value
        End If
        
        Cells(i, 11).Value = FormatPercent(Cells(i, 11).Value, 2)
        
        Next i
        
        Cells(2, 17).Value = FormatPercent(vInc, 2)
        Cells(3, 17).Value = FormatPercent(vDec, 2)
        Cells(4, 17).Value = vTot
        
        Cells(2, 16).Value = vTick2
        Cells(3, 16).Value = vTick1
        Cells(4, 16).Value = vTick3
        
        
    Next Current
    
    Call Module2.OptimizeCode_End

End Sub




