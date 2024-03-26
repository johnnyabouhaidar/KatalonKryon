
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys



WebUI.openBrowser('')

WebUI.navigateToUrl('https://iss-mea-188510.workflowcloud.com/forms/f2998e48-ca76-4628-81cf-5ca4925fd2cb')

WebUI.setText(findTestObject('Object Repository/CurrentApplication/CurrentForm/input_First Name'),'John')

WebUI.setText(findTestObject('Object Repository/CurrentApplication/CurrentForm/input_Last Name'),'Smith')

WebUI.setText(findTestObject('Object Repository/CurrentApplication/CurrentForm/textarea_Comments'),'hello')

WebUI.uploadFile(findTestObject('Object Repository/CurrentApplication/CurrentForm/input_Upload Document'),'C:\\Users\\johnny.abouhaidar\\Desktop\\myfiles\\katalon\\Test Run Report 26.pdf')

WebUI.click(findTestObject('Object Repository/CurrentApplication/CurrentForm/input_Submit'),'nan')

WebUI.closeBrowser()