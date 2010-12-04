
FEMhub.MeshEditor = Ext.extend(FEMhub.Window, {
    constructor: function(config) {
        config = config || {};

        Ext.apply(config, {
            title: "Mesh Editor",
            layout: 'fit',
            width: 870,
            height: 610,
            iconCls: 'femhub-mesheditor-icon',
            bodyCssClass: 'femhub-mesheditor-body',
            closable: true,
            onEsc: Ext.emptyFn,
            items: [{
                    "title": "Beta Version",
                    "html": '<table height="100%" width="100%" border="0" bgcolor="#728893"><tr><td valign="middle" align="center"><object type="application/x-shockwave-flash" data="/static/external/MeshEditor.swf" width="850" height="525"><param name="flashvars" value="output_cell=0&nodes=&elements=& boundaries=&curves=&var_name=m" /><p>Alternative ContentXX</p></object></tr></td></table>',
                    flex: 1,
                }],
            buttons: [{
                text: 'Close',
                handler: function() {
                    this.close();
                },
                scope: this,
            }],
        });

        FEMhub.MeshEditor.superclass.constructor.call(this, config);
    },
});

FEMhub.Modules.MeshEditor = Ext.extend(FEMhub.Module, {
    launcher: {
        text: 'Mesh Editor',
        icon: 'femhub-mesheditor-launcher-icon',
    },
    winCls: FEMhub.MeshEditor,
});
