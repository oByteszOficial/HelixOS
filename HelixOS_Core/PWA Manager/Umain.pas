unit Umain;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.WebBrowser,
  FMX.Controls.Presentation, FMX.Edit, FMX.StdCtrls;

type
  TForm1 = class(TForm)
    WebBrowser1: TWebBrowser;
    Edit1: TEdit;
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.fmx}

procedure TForm1.Button1Click(Sender: TObject);
begin

  if Edit1.Text = 'search' then
  begin

    WebBrowser1.URL := 'https://google.com';

  end;
  if Edit1.Text = 'docs' then
  begin

    WebBrowser1.URL := 'https://docs.google.com';

  end;

end;

end.
