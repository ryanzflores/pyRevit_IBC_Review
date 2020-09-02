import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

from pyrevit import UI
from pyrevit import script
xamlFile = script.get_bundle_file('ui.xaml')

import wpf
from System import Windows

import IBC

__title__ = 'Chapter\n5\nHelper'

__doc__ = "This tool helps you quickly calculate your building's" \
          'maximum height, stories, and area.'

# To use additional codes, make a module for the code and include its name in this tuple
available_codes = ('IBC', '')


class MyWindow(Windows.Window):
    current_table = None

    groups = None

    uses = None

    types = None

    # Tuple if all uses of the group have the same sprinklers, dict if some uses have different sprinklers
    sprinklers = None

    def __init__(self):
        wpf.LoadComponent(self, xamlFile)

        self.setup_combobox()

    @property
    def selected_code(self):
        return self.code_cb.SelectedItem

    @property
    def selected_group(self):
        return self.group_cb.SelectedItem

    @property
    def selected_use(self):
        return self.use_cb.SelectedItem

    @property
    def selected_type(self):
        return self.type_cb.SelectedItem

    @property
    def selected_sprinkler(self):
        return self.sprinkler_cb.SelectedItem

    def setup_combobox(self):
        self.code_cb.ItemsSource = available_codes
        self.group_cb.ItemsSource = self.groups
        self.use_cb.ItemsSource = self.uses
        self.type_cb.ItemsSource = self.types
        self.use_cb.IsEnabled = False

    def code_changed(self, sender, args):
        """Upon the code combobox being changed, sets groups and types to appropriate values,
        then calls group_changed to set the appropriate use and sprinkler values"""
        self.current_table = __import__("IBC")

        self.groups = self.current_table.table_info.keys()
        self.groups.sort()
        self.uses = None
        self.types = self.current_table.table_types

        self.setup_combobox()

    def group_changed(self, sender, args):
        """Upon the group combobox being changed, updates use options accordingly"""
        group = self.selected_group

        if group in self.groups:
            # If no uses available for current group
            if not self.current_table.table_info[group][0]:
                self.uses = None
                self.use_cb.ItemsSource = self.uses
                self.use_cb.IsEnabled = False

            # If there are uses specified for current group
            else:
                self.uses = self.current_table.table_info[group][0]
                self.use_cb.ItemsSource = self.uses
                self.use_cb.IsEnabled = True

            self.sprinklers = self.current_table.table_info[group][1]
        else:
            self.use_cb.ItemsSource = None
            self.use_cb.IsEnabled = False

        # Update sprinklers if necessary
        self.use_changed(None, None)

    def use_changed(self, sender, args):
        """Upon the use combobox being changed, updates sprinkler options for group 'R'"""
        use = self.selected_use

        self.sprinkler_cb.IsEnabled = True
        sprinkler_source = []

        # Handle case where each use has the same set of sprinklers
        if type(self.sprinklers) is tuple:
            for sprinkler in self.sprinklers:
                sprinkler_source.append(self.current_table.table_sprinklers[sprinkler])

        # Handle case where there are different sprinklers for different uses && use is selected
        elif type(self.sprinklers) is dict and use is not None:
            for sprinkler in self.sprinklers[use]:
                sprinkler_source.append(self.current_table.table_sprinklers[sprinkler])

        # Handle case where there are different sprinklers, BUT use is not selected
        else:  # type(self.sprinklers) is dict and use is None
            sprinkler_source = None
            self.sprinkler_cb.IsEnabled = False

            self.sprinkler_cb.ItemsSource = sprinkler_source
            return

        self.sprinkler_cb.ItemsSource = sprinkler_source

    def compute(self, sender, args):
        """When user presses continue, if all fields are filled, shows the user the max allowed
        height, stories, and area for their building"""
        group = self.selected_group
        use = self.selected_use
        sprinkler = self.selected_sprinkler.split(':')[0].split('/')[0]
        type = self.selected_type

        if not group or not type or not sprinkler:
            return

        self.current_table.show_results(group, use, sprinkler, type)


MyWindow().ShowDialog()
